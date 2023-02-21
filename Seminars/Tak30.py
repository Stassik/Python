"""
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""
def fill_list(x, y, z):
    x_list = list()
    x_list.append(y)
    for i in range(1, x):
        x_list.append(x_list[i-1]+z)
    return x_list

a_1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность чисел: "))
n = int(input("Введите количество элементов массива: "))

my_list = fill_list(n, a_1, d)
print(my_list)
