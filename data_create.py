import datetime
now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

def set_title(): 
    title = input('Введите название заметки: ')
    return title

def set_data(): 
    data = input('Введите текст заметки: ')
    return data

def set_cur_date():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

# print now.strftime("%d-%m-%Y %H:%M")
# Текущая дата и время с использованием strftime: 18-11-2015 16:15
