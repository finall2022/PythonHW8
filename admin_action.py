import os
from tokenize import Name


def new_reader():
    reader_card = input('Номер читательского билета: ')
    temp_data = open('base_readers.txt', 'a', encoding="utf-8")
    with open(reader_card + '.txt', 'a', encoding="utf-8") as data:
        data.write('\n')
        temp_data.write('\n')
        data.write(reader_card)
        data.write(', ')
        temp_data.write(reader_card)
        temp_data.write(', ')
        Fam = input('Фамилия: ')
        data.write(Fam)
        data.write(', ')
        temp_data.write(Fam)
        temp_data.write(', ')
        Name = input('Имя: ')
        data.write(Name)
        data.write(', ')
        temp_data.write(Name)
        temp_data.write(', ')
        Otch = input('Отчество: ')
        data.write(Otch)
        data.write(', ')
        temp_data.write(Otch)
        temp_data.write(', ')
        Phone = input('Телефон: ')
        data.write(Phone)
        data.write(', ')
        temp_data.write(Phone)
    temp_data.close()


def new_book(file):
    with open(file, 'a', encoding="utf-8") as data:
        data.write("\n")
        data.write(input('Номер в каталоге: '))
        data.write(', ')
        data.write(input('Автор: '))
        data.write(', ')
        data.write(input('Название: '))


def book_out(file):
    with open("base_books.txt", 'r', encoding="utf-8") as data_cat:
        book_number = input('Введите номер книги в каталоге: ')
        for line in data_cat:
            if book_number in line:
                book_out = (line)
            else:
                print('Нет такой книги!!!')
        with open(file, 'a', encoding="utf-8") as data:
            data.write("\n")
            data.write(book_out)


def book_in(file):
    book_number = input('Введите номер книги в каталоге')
    temp_data = open('temp.txt', 'w', encoding="utf-8")
    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            if book_number not in line:
                temp_data.write(line)

    temp_data.close()
    os.remove(file)
    os.rename('temp.txt', file)


def viewer(file):
    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            print(line)
