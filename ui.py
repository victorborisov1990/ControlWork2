from logger import input_data, print_data, find_data, delete_data, change_data
#добавть проверку вводимой команды, при вводе ерунды падает
def interface(): #три кавычки сохраняют форматирование при выводе
    def command_checker(number):
        while number < 1 or number > 6:
            print('******************************************')
            print("""Доступные команды: 
             1 - выход
             2 - запись данных 
             3 - печать данных 
             4 - поиск данных 
             5 - удаление данных
             6 - редактирование данных
             """)
            print('Введите номер команды: ')
            number = int(input())# нужна обработка исключений, проверка что введено число
        return number

    command_number = 0
    
    while command_number != 1:
        command_number = 0
        command_number = command_checker(command_number)
        if command_number == 2:
            input_data()
        elif command_number == 3:
            print_data()
        elif command_number == 4:
            print('Введите строку поиска: ')
            poisk = input()
            find_data(poisk)
        elif command_number == 5:
            print('Введите строку для удаления: ')
            del_str = input()
            delete_data(del_str)
        elif command_number == 6:
            print('Введите строку для редактирования: ')
            chng_str = input()
            change_data(chng_str)
        #нужен else на случай несуществующей команды 
    print('Выход из программы')
    