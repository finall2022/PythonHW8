import admin_action
from os import listdir


def admin():
    password = '12345'
    admin_pass = input('Введите пароль администратора - 12345: ')
    if admin_pass == password:
        n = "-1"
        while n != "0":
            print('Меню администратора')
            print('\t1. Новый читатель')
            print('\t2. Выдача книг')
            print('\t3. Возврат книг')
            print('\t4. Карточка читателя')
            print('\t5. Каталог книг')
            print('\t6. Поступление книг')
            print('\t0. Возврат в предыдущее меню')
            n = input('Выберите вариант: ')
            if n == "1":
                admin_action.new_reader()
            if n == "2":
                reader_card = input('Номер читательского билета: ')
                path = reader_card + '.txt'
                if path in listdir():
                    admin_action.book_out(path)
                else:
                    print('Неверный номер читательского билета')
            if n == "3":
                reader_card = input('Номер читательского билета: ')
                path = reader_card + '.txt'
                if path in listdir():
                    admin_action.book_in(path)
                else:
                    print('Неверный номер читательского билета')
            if n == "4":
                reader_card = input('Номер читательского билета: ')
                path = reader_card + '.txt'
                if path in listdir():
                    admin_action.viewer(path)
                else:
                    print('Неверный номер читательского билета')
            if n == "5":
                admin_action.viewer('base_books.txt')
            if n == "6":
                admin_action.new_book('base_books.txt')
    else:
        print('Неверный пароль')
