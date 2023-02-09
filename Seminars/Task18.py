"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел A i. 
Последняя строка содержит число X
"""

from random import randint

n = int(input("Введите длину массива: "))
x = int(input("Введите число: "))
m = int(input("Введите максимальное число: "))
my_list = [randint(0, m) for _ in range(n)]
print(f"Массив: {my_list}")

num = my_list[0]
count = m
for i in range(n):
    if my_list[i] > x:
        if count > my_list[i]-x:
            count = my_list[i]-x
            num = my_list[i]
            index = i
    else:
        if count > x-my_list[i]:
            count = x-my_list[i]
            num = my_list[i]
            index = i          
    
print(f"Минимальная разница: {count}")
print(f"Искомое число: {num} под индексом {index}")