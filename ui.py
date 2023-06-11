from logger import input_data, print_data, find_data, delete_data, change_data
#добавть проверку вводимой команды, при вводе ерунды падает
def interface(): #три кавычки сохраняют форматирование при выводе
    def command_checker(number):
        while number < 1 or number > 6:
            print('******************************************')
            print("""Доступные команды: 
             1 - выход
             2 - добавить заметку 
             3 - показать список заметок 
             4 - поиск заметки 
             5 - удаление заметки
             6 - редактирование заметки
             """)
            print('Введите номер команды: ')
            try:
                number = int(input())#обработка исключений, проверка что введено число
            except:
               print('введена неверная команда')
               number = 0 
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
            print('Введите дату в формате "дд","дд-мм" или "дд-мм-гггг" для поиска: ')
            poisk = input()
            find_data(poisk)
        elif command_number == 5:
            delete_data()
        elif command_number == 6:
            change_data()
    print('Выход из программы')
    