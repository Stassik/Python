"""
Задача 2.
Найдите сумму цифр трехзначного числа. 

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
number = int(input("Введите трехзначное число: "))


def calc_sum(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num//10
    return sum


if number > 999 or number < 100:
    print("Вы ввели не трехзначное число.")
else:
    total = calc_sum(number)
    print(total)
