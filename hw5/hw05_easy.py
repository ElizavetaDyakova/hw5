# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

lst = [random.randint(-10, 10) for _ in range(10)] #заполняем список рандомными числами
print('Список: ', lst) #выводим список
lstkv = [el*el for el in lst] #возводим элементы в квадрат
print('Список квадратов чисел: ', lstkv) #Выводим новый список

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.



fruits = ['apple', 'banana', 'mango', 'avocado', 'peach',
           'pear', 'watermelon', 'lemon', 'mandarin', 'orange', 'lime'] #создаем список фруктов
#генерируем списки с фруктами
spisok1 = random.sample(fruits,6)
spisok2 = random.sample(fruits,6)
#вывод списков
print('Список 1: ', " ".join(spisok1))
print('Список 2: ', " ".join(spisok2))
#ищем повторяющиеся элементы
spisok3 = [fruit for fruit in spisok1 if fruit in spisok2]
#вывод
print('Повторяющиеся фрукты: ', " ".join(spisok3))




# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst = [random.randint(-100, 100) for _ in range(10)] #заполняем список рандомными числами
print('Список: ', lst) #выводим список
lst2 = [el for el in lst if el%3==0 and el>0 and el%4!=0] #создаем список элементов, соответствующих условию
print(lst2) #вывод