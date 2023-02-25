"""
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи
(Например имя или фамилию человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

#Импорт данных в справочник

def export_to_phonebook(new_line):
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.writelines(new_line)

def import_to_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        contact = data.readline()
        print(contact)
        
def input_contact():
    new_contact = dict()
    new_contact['Фамилия'] = ''
    new_contact['Имя'] = ''
    new_contact['Отчество'] = ''
    new_contact['Телефон'] = ''

    for item in new_contact:
        new_contact[item] = input(f'{item}: ')
        export_to_phonebook(" {}: {} |".format(item, new_contact[item]))


#input_contact()
import_to_phonebook()


    



        

