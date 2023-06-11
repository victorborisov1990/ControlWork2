import os
from data_create import  set_title, set_data, set_cur_date
file_name = 'notes\\data.csv'


def print_data(cmd=0):#функция вывода списка заметок
    if os.path.exists(file_name):
        print('Список заметок:')
        print('id \t название \t дата изменения')
        print()
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines() #возвращает массив строк
            # проверять, если массив пустой - писать, что файл пуст
            if len(list_data) == 0:
                print('Файл пуст.')
                return 1
            else:#если файл не пустой
                for line in list_data:
                    id,title,*_,change_time = line.split(';')#берем 1,2 и послед эмлементы. Если текст заметки
                    #будет содержать ';' разбитый на части текст упакуется в переменную "_"
                    print(id,'\t',title,'\t',change_time)
                # выбрать какую заметку вывести на экран
                if cmd == 0:
                    print('Введите номер заметки, которую хотите посмотреть: ')
                    index = 0
                    index_list = [i for i in range (0, len(list_data))]#список индексов заметок
                    try:
                        index = int(input())
                    except:
                        print('Введен недопустимый символ ')
                    if index in index_list: #если введенный индекс существует в файле
                        print_note(list_data[index])
                    else:
                        print('Введен неверный индекс ')
                return 0
    else:
        print('Файл не существует!')
        return 2


def input_data():#функция добавления информации в файл
    # если файл существует, то определяем номер для новой заметки:
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:    
            list_data = file.readlines()
            id = len(list_data)#количество заметок в файле (строк) - индекс для новой строки
    else:
        id = 0 # если файл не существует, то начинаем с 0
    with open(file_name, 'a', encoding='utf-8') as file:
        title = set_title()#название заметки
        data = set_data()#содержимое заметки
        file.write(f'{id};{title};{data};{set_cur_date()}\n')
    
        

def find_data(find_string):#функция поиска заметки (по дате) find_string должна иметь формат "дд-мм-гггг"
    if os.path.exists(file_name):#если файл существует
        print()
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()
            found_index = [] #список индеков строк, в которых нашлись совпадения
            for i in range(len(list_data)):
                _,title,*_,change_time = list_data[i].split(';')
                if  change_time.startswith(find_string): #если дата изменения начинается с искомой даты
                    found_index.append(i)#сохраняем индекс строки, в которых нашлись совпадения
                    print(i,'\t',title,'\t',change_time)
            if len(found_index) == 0:
                print('Ничего не найдено!')
            else:
                print()
                print(f'Найдено: {len(found_index)} записей')
                # выбор открыть заметку из найденных:
                print('Введите номер заметки, которую хотите посмотреть: ')
                invalid_index = True
                index = 0
                while invalid_index: #пока не будет корректный ввод индекса, повторять ввод
                    try:
                        index = int(input())
                        invalid_index = False
                    except:
                        print('Введен недопустимый символ ')
                        invalid_index = True
                if index in found_index: #если введенный индекс в списке найденных
                    print_note(list_data[index])
                else:
                    print('Введен неверный индекс ')         
    else:
        print('Файл не существует!')
    


def delete_data():#функция удаления заметки
    file_state = print_data(1)#вывод списка заметок без предложения выбора заметки для просмотра
    list_to_delete =  []
    if file_state == 0:#если файл существует и не пустой, прошла печать списка
        print('Введите номера заметок для удаления через пробел: ')
        try:
            list_to_delete = list(map(int, (input().split())))#считываем строку и создаем из нее список индексов
        except:
            print('Введен недопустимый символ ')
        list_to_delete.sort(reverse=True)#сортируем по убыванию, чтобы удалять с конца
        if len(list_to_delete):#если список индексов на удаление не пустой
            with open(file_name, 'r', encoding='utf-8') as file:
                list_data = file.readlines()
                index_list = [i for i in range (0, len(list_data))] #список номеров строк (заметок)
                for ind_to_del in list_to_delete:
                    if ind_to_del in index_list:# проверка, что ввели индекс из списка, а не случайный
                        list_data.pop(ind_to_del)
                    else:
                        print('Введен неверный индекс ')
            with open(file_name, 'w', encoding='utf-8') as file:
                file.writelines(list_data)#запись отредактированного списка обратно в файл
            index_refresh()
            print('готово')
        else:#если список индексов на удаление пустой
            print('не были выбраны строки. выход из режима удаления')


def change_data():#функция редактирования информации из файла
    # после редактирования подменять дату на текущую
    file_state = print_data(1)#вывод списка заметок без предложения выбора заметки для просмотра
    if file_state == 0:#если файл существует и не пустой, прошла печать списка
        index = 0
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()
            index_list = [i for i in range (0, len(list_data))]#список индексов заметок
        print('Введите номер заметки для редактирования: ')
        try:
            index = int(input())
        except:
            print('Введен недопустимый символ ')
        if index in index_list: #если введенный индекс существует в файле
            print_note(list_data[index])
            id,title,*data,_ = list_data[index].split(';')#дату можно не сохранять, после редакт-я она обновится
            new_data = ';'.join(data)# восстановление текста заметки из списка в строку
                # проверить как будет соединять список одинарной длины
            print("""Доступные команды: 
                    1 - выйти из режима редактирования
                    2 - редактировать название
                    3 - редактировать текст заметки 
                    """)
            number = 0 #инициализация номера команды
            while number != 1:#до выхода из редактирования можно редактировать любые поля
                number = 0#обнуление номера после каждой выполненной команды
                while number < 1 or number > 3: #введен не существующий номер команды, повторить ввод
                    print('Введите номер команды: ')
                    try:
                        number = int(input())
                    except:
                        print('Введен недопустимый символ ')
                if number == 2:
                    print('Введите новое называние заметки: ')
                    title = input()
                elif number == 3:
                    print('Введите новый текст заметки: ')
                    new_data = input()
            # выход из режима редактирования
            list_data[index] =  (f'{id};{title};{new_data};{set_cur_date()}\n')# вставка по индексу редактированной сроки заменит неактуальную
            with open(file_name, 'w', encoding='utf-8') as file:
                file.writelines(list_data)#запись отредактированного списка обратно в файл
                print()
                print('готово!')
        else:
            print('Введен неверный индекс ')
    else:
        print('Файл пустой или не существует')        
            
def print_note(csv_string):# функция вывода выбранной заметки
    _,_,*note,_ = csv_string.split(';') # нужный фрагмент стоит между 1,2 и последним элементами строки.
    # текст может содержать ; и будет разделен, поэтому нужный фрагмент нужно хранить как список
    print(*note,sep=';')


def index_refresh():# функция переопределения id после удаления
    with open(file_name, 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        for i in range (0, len(list_data)):
            line = list_data[i].split(';',1)# строка станет списком из 2х элем-в: id и все остальное
            line[0] = str(i)+';'
            list_data[i] = ''.join(line)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(list_data)#запись отредактированного списка обратно в файл
        
