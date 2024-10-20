'''библиотека Pillow позволяет удобно работать с изображениями. Главной помощью в этом является класс Image
и его методы. например этот класс с помощью метода формат позволяет нам конвертировать изображение в другой
тип данных. С помощью size мы можем изменить размер фаайла. с помощью crop мы можем вырезать, обьединять.
для работы с изображениями оень удобен.'''

from PIL import Image

cartinca = Image.open('xh.jpeg')
l = cartinca.crop((25, 25, 75, 75))
l.show()  # просмаатриваать или легко нааходить изображения
print(cartinca.format, cartinca.size, cartinca.mode)  # gросмотр хаарактеристик
cartinca.resize((10, 10))  # изменение размера
cartinca.save('resized.jpeg')  # и конвертирование
