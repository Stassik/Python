"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список чисел. 
Все числа списка находятся на разных строках.
"""

def fill_list(x):
    x_list = list()
    for i in range(x):
        x_list.append(int(input(f"Введите {i+1} число: ")))
    return x_list

def count_num(x_list):
    count = 0
    for i in range(len(x_list)-1):   
        if x_list[i]==x_list[i+1]:
            count += 1
    return count

n = int(input("Введите длину массива: "))
n_list = sorted(fill_list(n))
total = count_num(n_list)
print(n_list)
print(total)