"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы
"""

def rec_sum(x, y, total=0):
    if x>=1 or y>=1:
        total +=1
        if x>y:
            x -=1
        else:
            y -= 1
        return rec_sum(x, y, total)
    return total            

a = int(input("Введите число А: "))
b = int(input("ВВедите число В: "))

while a <0 or b<0:
    print("Вы ввели отрицательное число.")
    if a<0:
        a = int(input("Введите число А: "))
    else:
        b = int(input("ВВедите число В: "))

total = rec_sum(a, b)
print(total)
