"""
1. За день машина проезжает n километров. 
Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

Input:
n = 700
m = 750
Output:
2
"""

n = int(input("Введите n"))
m = int(input("Введите m"))
print(m//n + (m % n != 0))