"""
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""
word = "a a a b c a a d c d d"
my_list = word.split()
result = ''
print(my_list)

d = dict()

for i in range(len(my_list)):
    if my_list[i] not in d:
        d[my_list[i]] = 1
        result += f'{my_list[i]} '
    else:
        result += f'{my_list[i]}_{d[my_list[i]]} '
        d[my_list[i]] += 1

print(result)
print(d)
