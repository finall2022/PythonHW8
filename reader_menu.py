from os import listdir
import admin_action


def reader():
    reader_card = input('Номер читательского билета: ')
    path = reader_card + '.txt'
    if path in listdir():
        n = '-1'
        while n != '0':
            print('Меню читателя')
            print('\t1. Карточка читателя')
            print('\t2. Каталог книг')
            print('\t0. Возврат в предыдущее меню')
            n = input('Выберите вариант: ')
            if n == '1':
                admin_action.viewer(path)
            if n == '2':
                admin_action.viewer('base_books.txt')
    else:
        print('Неверный номер читательского билета')
