"""
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? 
Помогите ему!
Пользователь вводит одно число N – количество арбузов. 
Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза

Input: 5 -> 5 1 6 5 9
Output: 1 9

"""
import random
n = int(input("Введите количество арбузов: "))
weight = random.randint(1,9)
print(f"1 арбуз весит - {weight}")
max_weight = weight
min_weight = weight
for i in range(2, n+1):
    weight = random.randint(1,9)
    print(f"{i} арбуз весит {weight}")
    if weight > max_weight:
        max_weight = weight
    elif weight < min_weight:
        min_weight = weight
print(f"\n Максимальная масса - {max_weight}, минимальная масса - {min_weight}")
           
    