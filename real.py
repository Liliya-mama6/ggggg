import fastapi
from pydantic import BaseModel
from fastapi import Path, HTTPException, Body, Request
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = fastapi.FastAPI()

# $ python3 -m uvicorn iscandar:app
users = []

a=Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int = None
    nick: str
    year: int


@app.get('/')
async def welcome(request:Request) -> HTMLResponse:
    return a.TemplateResponse('users.html', {'request':request, 'users':users})


@app.get('/user/{user_id}')
async def get(request:Request, user_id:int) -> HTMLResponse:
    try:
        return a.TemplateResponse('users.html', {'request':request, 'user':users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')

@app.post(path='/user/{username}/{age}')
async def create(username: str, age: int) -> User:
    user: User = User(id=len(users) + 1, nick=username, year=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update(user_id, username, age) -> str:
    try:
        a:User=User(id=user_id, nick=username, year=age)
        users[user_id] = a
        return 'all was successful'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete(user_id) -> str:
    global users
    try:
        new_users = users[:user_id - 1] + users[user_id:]
        users = new_users
        return 'User was deleted'
    except:
        HTTPException(status_code=404, detail="User was not found")
