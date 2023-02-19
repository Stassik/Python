"""1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)"""

from random import randint


"""def find_num(list_x):
    new_list = list()
    for i in list_x:
        if i % 2 == 0:
            new_list.append((i, i*i,))
    return new_list

my_list = [randint(0, 100) for _ in range(5, 11)]

print(my_list)
print(find_num(my_list))   
    
"""
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

my_list = [randint(1, 10) for _ in range(10)]

res = select(int, my_list)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x * x), res)
print(res)


