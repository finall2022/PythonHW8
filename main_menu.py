import admin_menu
import reader_menu


def m_menu():
    n = "-1"
    while n != "0":
        print('Главное меню')
        print('Войти как:')
        print('\t1. Администратор')
        print('\t2. Читатель')
        print('\t0. Выход')
        n = input('Выберите вариант: ')
        if n == "1":
            admin_menu.admin()
        if n == "2":
            reader_menu.reader()
