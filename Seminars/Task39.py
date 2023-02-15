"""
Даны два массива чисел. 
Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. 
Пользователь вводит число N - количество элементов в первом массиве, 
затем N чисел - элементы массива. 
Затем число M - количество элементов во втором массиве. Затем элементы второго массива
"""
def find_dif(x, x_list, y_list, z_list):
    for i in range(x):
        if x_list[i] not in y_list:
            z_list.append(n_list[i])
    return z_list

def fill_list (x, x_list):
    for i in range(x):
        x_list.append(int(input(f"Введите {i+1} число: ")))
    return x_list    

n = int(input("Введите длину массива N: "))
n_list = list()
n_list = fill_list(n, n_list)
m = int(input("Введите длину массива M: "))
m_list = list()
m_list = fill_list(m, m_list)
dif_list = list()
print(find_dif(n, n_list, m_list, dif_list))
