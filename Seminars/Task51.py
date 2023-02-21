"""
Напишите функцию same_by(characteristic, objects), которая проверяет, 
все ли объекты имеют одинаковое значение некоторой характеристики, 
и возвращают True, если это так.

Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его
характеристику.

Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print(‘same’)
else:
    print(‘different’)

Вывод:
same
"""
"""def same_by(characteristic, objects):
    if not objects: # Если список пустой, то все элементы одинаковы
        return True
    characteristic_values = [characteristic(obj) for obj in objects]
    return all(x == characteristic_values[0] for x in characteristic_values)"""

def same_by(func, list1): 
    new_list1 = list(filter(func, list1)) 
    return len(new_list1) == len(list1) or len(new_list1) == 0 

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")