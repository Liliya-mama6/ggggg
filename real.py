class House:
    houses_history=[]
    def __new__(cls, name, nmb):
        cls.houses_history.append(name)
        return super().__new__(cls)
    def __init__(self, name, nmb):
        self.name=name
        self.nmb=nmb
    def go_to(self, nf):
        if nf>self.nmb or nf<1:
            print("Такого этажа не существует")
        else:
            for i in range(1, nf+1):
                print(i)
    def __len__(self):
        return self.nmb
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей {self.nmb}.'
    def __eq__(self, other):
        if isinstance(other, House):
            a=True
        else:
            a=False
        if a==True and self.nmb == other.nmb:
            return True
        elif a==False:
            return 'Объект класса House сраавнивается только с подобными объектами'
        else:
            return False
    def __lt__(self, other):
        if isinstance(other, House):
            a = True
        else:
            a = False
        if a == True and self.nmb < other.nmb:
            return True
        elif a == False:
            return 'Объект класса House сраавнивается только с подобными объектами'
        else:
            return False
    def __le__(self, other):
        if isinstance(other, House):
            a = True
        else:
            a = False
        if a == True and self.nmb <= other.nmb:
            return True
        elif a == False:
            return 'Объект класса House сраавнивается только с подобными объектами'
        else:
            return False
    def __gt__(self, other):
        if isinstance(other, House):
            a = True
        else:
            a = False
        if a == True and self.nmb > other.nmb:
            return True
        elif a == False:
            return 'Объект класса House сраавнивается только с подобными объектами'
        else:
            return False
    def __ge__(self, other):
        if isinstance(other, House):
            a = True
        else:
            a = False
        if a == True and self.nmb >= other.nmb:
            return True
        elif a == False:
            return 'Объект класса House сраавнивается только с подобными объектами'
        else:
            return False
    def __ne__(self, other):
        if isinstance(other, House):
            a = True
        else:
            a = False
        if a == True and self.nmb != other.nmb:
            return True
        elif a == False:
            return 'Объект класса House сраавнивается только с подобными объектами'
        else:
            return False
    def __add__(self, value):
        if isinstance(value, int):
            a=True
        else:
            a=False
        if a==True:
            self.nmb+=value
        else:
            return 'нельзя прибавить не число к количеству этажей'
        return self
    def __radd__(self, value):
        a=True
        if isinstance(value, int):
            a=True
        else:
            a=False
        if a==True:
            self.nmb+=value
        else:
            return 'нельзя прибавить не число к количеству этажей'
        return self
    def __iadd__(self, value):
        a=True
        if isinstance(value, int):
            a=True
        else:
            a=False
        if a==True:
            self.nmb+=value
        else:
            return 'нельзя прибавить не число к количеству этажей'
        return self
    def __del__(self):
        print(self.name, 'Снесен но останется в истории')
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)