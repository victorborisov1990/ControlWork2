import os
import datetime
from data_create import  set_title, set_data
file_name = 'notes\\data.csv'
now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
# print now.strftime("%d-%m-%Y %H:%M")
# Текущая дата и время с использованием strftime: 18-11-2015 16:15

def print_data():#функция вывода содержимого файла в консоль
    if os.path.exists(file_name):
        print('Вывод данных из файла:')
        print()
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines() #возвращает массив строк
            # проверять, если массив пустой - писать, что файл пуст
            if len(list_data) == 0:
                print('Файл пуст.')
            else:
                for line in list_data:
                    
                    print(line)
    else:
        print('Файл не существует!')


def input_data():#функция добавления информации в файл
    print('Введите данные:')
    id = 0   #нужна глобальная переменная которая хранит индекс для новой строки
    title = set_title()#название заметки
    data = set_data()#содержимое заметки
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{id};{title};{data};{now}\n') 
        

def find_data(find_string):#функция поиска строки в содержимом файла
    if os.path.exists(file_name):#если файл существует
        print()
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()
            find_count = 0#счетчик найденных записей
            found_index = []#список индеков строк, в которых нашлись совпадения
            find_string = find_string.lower()#приведение к нижнему регистру
            for i in range(len(list_data)):
                line = list_data[i].lower()#приведение к нижнему регистру
                if find_string in line:
                    print(i, line)
                    find_count +=1#подсчет найденных записей
                    found_index.append(i)#сорхраняем индекс строки, в которых нашлись совпадения
            if find_count == 0:
                print('Ничего не найдено!')
            else:
                print()
                print(f'Найдено: {find_count} записей')
    else:
        print('Файл не существует!')
    return found_index # проверить. выпадает с ошибкой, если ничего не найдено или если нет файла
                        # почемуто вывел найденную строку, сменив регистр
                        # при этом поиск работает не смотря на регистр 


def delete_data(delete_string):#функция удаления информации из файла
    index_list = find_data(delete_string)
    if not len(index_list):#если список пустой
        print('Нет данных для удаления')
    else:
        print('Введите номера записей для удаления через пробел: ')
        list_to_delete = list(map(int, (input().split())))#считываем строку и создаем из нее список индексов
        list_to_delete.sort(reverse=True)#сортируем по убыванию, чтобы удалять с конца
        if len(list_to_delete):#если список не пустой
            with open(file_name, 'r', encoding='utf-8') as file:
                list_data = file.readlines()
                for ind_to_del in list_to_delete:
                    if ind_to_del in index_list:# проверка, что ввели индекс из найденных, а не случайный
                        list_data.pop(ind_to_del)
                    else:
                        print('Введен неверный индекс ')
            with open(file_name, 'w', encoding='utf-8') as file:
                file.writelines(list_data)#запись отредактированного списка обратно в файл
            print('готово')
        else:
            print('не были выбраны строки. выход из режима удаления')


def change_data(change_string):#функция редактирования информации из файла
    index_list = find_data(change_string)
    if not len(index_list):#если список пустой
        print('Нет данных для изменения')
    else:
        print('Введите номер записи для редактирования: ')
        str_to_change = int(input())#номер строки, которую нужно отредактировать
        if str_to_change in index_list:#если введенный индекс строки в списке найденных
            with open(file_name, 'r', encoding='utf-8') as file:
                list_data = file.readlines()
                line_to_chng = list_data[str_to_change].split(';')
                print(line_to_chng)
                print("""Доступные команды: 
                        1 - редактировать фамилию
                        2 - редактировать имя
                        3 - редактировать отчество 
                        4 - редактировать телефон
                        5 - выйти из режима редактирования 
                        """)
                # print('Введите номер команды: ')
                # number = int(input())
                # while number < 1 or number > 5:
                #     print('Введите корректный номер команды: ')
                #     number = int(input())
                number = 0 #инициализация номера
                while number != 5:#до выхода из редактирования можно редактировать любые поля
                    number = 0#обнуление номера после каждой выполненной команды
                    while number < 1 or number > 5:
                        print('Введите номер команды: ')
                        number = int(input())
                    if number == 1:
                        print('Введите новую фамилию: ')
                        line_to_chng[0] = input()
                    elif number == 2:
                        print('Введите новое имя: ')
                        line_to_chng[1] = input()
                    elif number == 3:
                        print('Введите новое отчество: ')
                        line_to_chng[2] = input()
                    elif number == 4:
                        print('Введите новый телефон: ')
                        phone = input()
                        line_to_chng[3] = phone + '\n'
                list_data.pop(str_to_change)#удаление строки с неактуальной информацией
                list_data.append(';'.join(line_to_chng))#соединение списка обратно в строку с разделителем и добавление в конец массива
            with open(file_name, 'w', encoding='utf-8') as file:
                file.writelines(list_data)#запись отредактированного списка обратно в файл
                print()
                print('готово!')
        else:
            print('Введен неверный индекс ')
            
