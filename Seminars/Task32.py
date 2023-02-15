"""
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""

from random import randint

def find_index(x, x_list, min, max):
    new_list = list()
    for i in range(x):
        if  min < x_list[i] < max:
            new_list.append(i)
    return new_list        

n = int(input("Введите длину массива: "))
min_num = int(input("Введите минимальное число диапазона: "))
max_num = int(input("Введите максимальное число диапазона: "))

my_list = [randint(-10, 10) for _ in range(n)]
print(my_list)
index_list = find_index(n, my_list, min_num, max_num)
print(index_list)


