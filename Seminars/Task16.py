"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
3
-
"""
from random import randint

n = int(input("Введите длину массива: "))
x = int(input("Введите искомое число от 1 до 9: "))
my_list = [randint(0, 10) for _ in range(n)]
print(f"Массив: {my_list}")

count = len([1 for i in range(n) if my_list[i] == x])
print(count)
temp = my_list.count(x) #метод count
print(temp)