import db
from utils import print_menu, print_books


def add_book() -> None:
    name = input('Название книги: ')
    author = input('Автор книги: ')
    year = input('Год написания книги: ')
    while not year.isdigit():
        print('Нужно ввести число!')
        year = input('Год написания книги: ')
    db.add_book(name, author, year)
    print('Книга добавлена успешно.')


def delete_book() -> None:
    book_id = input('ID книги: ')
    while not book_id.isdigit():
        print('Нужно ввести число!')
        book_id = input('ID книги: ')
    db.delete_book(book_id)
    print('Книга удалена успешно.')


def search_books() -> None:
    key = input('Имя автора, название книги или год выпуска: ')
    books = db.search_books(key)
    if not books:
        print('По вашему запросу ничего не найдено.')
        return
    print('Результаты поиска:')
    print_books(books)


def print_all_books() -> None:
    print('Список всех книг:')
    books = db.get_all_books()
    print_books(books)


def change_book_status() -> None:
    book_id = input('ID книги: ')
    while not book_id.isdigit():
        print('Нужно ввести число!')
        book_id = input('ID книги: ')
    new_status = input('Новый статус книги: ')
    try:
        db.change_book_status(book_id, new_status)
        print('Статус книги изменен успешно.')
    except Exception as e:
        print(f'Ошибка: {e}')
    


while True:
    print_menu()
    option = input('Введите номер команды: ')
    while not option in map(str, range(1, 7)):
        print('Неверная команда, попробуйде снова')
        option = input('Введите номер команды: ')

    if option == '1':
        try:
            add_book()
        except Exception as e:
            print(f'Ошибка: {e}')

    elif option == '2':
        try:
            delete_book()
        except Exception as e:
            print(f'Ошибка: {e}')

    elif option == '3':
        search_books()

    elif option == '4':
        try:
            print_all_books()
        except Exception as e:
            print(f'Ошибка: {e}')

    elif option == '5':
        change_book_status()

    elif option == '6':
        print('See you next time!')
        break

    stop = input('Нажмите Enter, чтобы продолжить...')
