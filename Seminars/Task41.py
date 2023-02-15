"""
Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит
количество элементов, у которых два соседних и, 
при этом, оба соседних элемента меньше данного. 
Сначала вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. 
Массив состоит из целых чисел.
"""
def fill_list(x):
    x_list = list()
    for i in range(x):
        x_list.append(int(input(f"Введите {i+1} число: ")))
    return x_list

def count_num(x_list):
    count = 0
    for i in range(1, len(x_list)-1):   
        if x_list[i]>x_list[i+1] and x_list[i]>x_list[i-1]:
            count += 1
    return count        

n = int(input("Введите длину массива: "))
n_list = fill_list(n)
total = count_num(n_list)
print(n_list)
print(total)
