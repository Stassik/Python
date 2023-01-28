"""
Задача 6.
Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета
385916 -> yes
123456 -> no
"""

len_ticket = int(input("Введите количество цифр в номере билета: "))


def get_ticket_numbers(length):
    ticket_num = []
    for i in range(0, length):
        num = int(input(f"Введите цифру {i+1} в номере билета: "))
        if num >= 0 and num < 10:
            ticket_num.append(num)
        else:
            print("Введите положительные числа от 0 до 9")
            break

    return ticket_num


def find_sum1(ticket_num):
    sum1 = 0
    for i in range(0, len(ticket_num)//2):
        sum1 += ticket_num[i]
        print(sum1)
    return sum1


def find_sum2(ticket_num):
    sum2 = 0
    for i in range(-len(ticket_num)//2, 0):
        sum2 += ticket_num[i]
        print(sum2)

    return sum2


def check_the_ticket(sum1, sum2):
    if sum1 == sum2:
        print("Ура! У Вас счастливый билет!")
    else:
        print("К сожалению Ваш билет обычный.")


ticket_number = get_ticket_numbers(len_ticket)
print(ticket_number)

sum1_number = find_sum1(ticket_number)
sum2_number = find_sum2(ticket_number)
check_the_ticket(sum1_number, sum2_number)
