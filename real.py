from time import *

class User():
    def __init__(self, nick, passw, age):
        self.nick = nick
        self.password = passw
        self.age = age


class UrTube():
    current_user = None
    videos = []
    users = {}
    nicknames = []

    def register(self, name, password, age):
        if name in self.nicknames:
            print(f'Пользователь {name} уже существует')
        else:
            self.users[name] = [password, age]
            self.nicknames.append(name)
            self.current_user = name

    def log_in(self, name, password):
        if name in self.nicknames and hash(self.users[name][0]) == hash(password):
            self.current_user = name
        else:
            print('Неправильно введено имя или пароль')

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for i in range(len(video)):
            if isinstance(video[i], Video):
                self.videos.append([video[i].title, video[i].duration, video[i].adult_mode])
            else:
                print('Вы пытаетесь добавить не видео, просим это исправить. C уважением, администрация сайта UrTube')

    def get_videos(self, st):
        v = []
        for i in range(len(self.videos)):
            n = self.videos[i][0].upper()
            if st.upper() in n:
                v.append(self.videos[i][0])
        return v
    def watch_video(self, video):
        if self.current_user==None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for i in range(len(self.videos)):
                if video == self.videos[i][0] and self.videos[i][2]==True and self.users[self.current_user][1]<18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                elif video == self.videos[i][0] and self.videos[i][2]==True and self.users[self.current_user][1]>=18:
                    for i in range(1, self.videos[i][1]+1):
                        print(i, end=' ')
                        sleep(0.5)
                    print('Конец видео')


class Video():
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v2, v1)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('г'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
