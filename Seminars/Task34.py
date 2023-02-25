"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, 
то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. 
Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
если с ритмом все не в порядке
Ввод: 
пара-ра-рам рам-пам-папам па-ра-па-дам 

Вывод:
Парам пам-пам
"""
vowel_letters = ['а', 'у', 'о', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']
words_list = input("Введите фразу: ").split()
print(words_list)
count_list = set()
for i in range(0, len(words_list)):
    letters_list = list()
    word = words_list[i]
    count = 0

    for j in range(0, len(word)): #Разбиваем слово на буквы
        letters_list.append(word[j])

        for k in vowel_letters: # Считаем сколько в слове гласных букв (слогов)
            if k == word[j]:
                count += 1
    count_list.add(count)    
print(*count_list)

if len(count_list) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")    
     
    
         

    
