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

# Импорт данных в справочник


def input_contact():
    contact_elem = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    new_contact = list()
    for i in range(len(contact_elem)):
        new_contact.insert(i, input(f'{contact_elem[i]}: ').title())
    export_to_phonebook(new_contact)


def export_to_phonebook(new_line):
    with open('phonebook.txt', 'a+', encoding='utf-8') as data:
        data.writelines(' '.join(new_line)+'\n')


def import_to_phonebook():
    phonebook = dict()
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        contacts = data.readlines()
        for i in range(len(contacts)):
            phonebook[i] = contacts[i]
    return phonebook


def main_import_to_phonebook():
    phonebook = import_to_phonebook()
    for item in phonebook:
        print('{} | {}'.format(item+1, phonebook[item]))


def search_contact(some_str):
    phonebook = import_to_phonebook()
    count = 0
    print("\nРезультат поиска:")
    for i in phonebook:
        if some_str in phonebook[i]:
            print('{} | {}'.format(i+1, phonebook[i]))
            count+=1
    if count != 0:
        print(f'Всего найдено: {count}')
    else:
        print('Ничего не найдено')
        exit
 
def replace_phonebook(messege, new_phonebook):
    with open('phonebook.txt', 'w', encoding='utf-8') as data: 
        print(messege)   
        data.writelines(new_phonebook)

def delete_contact(some_str):
    search_contact(some_str)
    with open('phonebook.txt', 'r+', encoding='utf-8') as data:
        contacts = data.readlines()
        id_contact = int(input('\nВведите номер нужной записи: '))
        del contacts[id_contact-1]
    replace_phonebook('Удалено...', contacts)
    
        
def edit_contact(some_str):
    contact_elem = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    search_contact(some_str)
    with open('phonebook.txt', 'r+', encoding='utf-8') as data:
        contacts = data.readlines()
        id_contact = int(input('\nВведите номер нужной записи: '))
        contact = contacts[id_contact-1].split()
        print('\nЧто Вы хотите изменить?')
        user_choice = int(input('\n1 - фамилию\n2 - имя\n3 - отчество\n4 - телефон\n0 - отмена\n'))
        for i in range(len(contact_elem)):
            if i == (user_choice-1):    
                contact[i] = input(f'{contact_elem[i]}: ').title()
        contacts[id_contact-1] = (' '.join(contact)+'\n')
    replace_phonebook('Сохранено...', contacts)
        

def text():
   search_elem = input('\nВведите критерий поиска: ').title()
   return search_elem 

def phonebook_menu():
    user_choice = input('\n1 - показать все записи\n2 - создать новую запись\n3 - найти запись\n4 - удалить запись\n5 - изменить запись\n0 - закрыть программу\n')
    if user_choice == '1':
        main_import_to_phonebook()
        phonebook_menu()
    elif user_choice == '2':
        input_contact()
        phonebook_menu()
    elif user_choice == '3':
        search_elem = text()
        search_contact(search_elem)
        phonebook_menu()
    elif user_choice == '4':
        search_elem = text()
        delete_contact(search_elem)
        phonebook_menu()
    elif user_choice == '5':
        search_elem = text()
        edit_contact(search_elem)
        phonebook_menu()
    elif user_choice == '0':
        exit

def user_interface():
    header = 'Записная книжка'.center(50, '-')
    print(header)
    phonebook_menu()
    

user_interface()

