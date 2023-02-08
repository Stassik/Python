"""
Дан список чисел. 
Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
from random import randint

my_list = [randint(0, 10) for i in range(10)]
print(my_list)
new_list = set(my_list)
print(len(list(new_list)))