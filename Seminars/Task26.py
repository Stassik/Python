"""
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

def raise_to_degree(x, y, total=1 ):
    if y==1:
        return x
    if total >= x**y:
        return total
    total *= x
    return raise_to_degree(x, y, total)

num = int(input("Введите число: "))
deg = int(input("Введите степень: "))
total = raise_to_degree(num, deg)
print(total)
