def print_menu() -> None:
    print("\nМеню:")
    print("1 - Добавить книгу")
    print("2 - Удалить книгу")
    print("3 - Найти книгу")
    print("4 - Показать все книги")
    print("5 - Изменить статус книги")
    print("6 - Выйти\n")

def print_columns(spaces: int) -> None:
    ident = ' ' * spaces
    string = f'ID    {ident}TITLE {ident}AUTHOR{ident}YEAR  {ident}STATUS'
    print(string)

def cut(string: str) -> str:
    DOTS_NUM: int = 2
    LENGTH: int = 13
    dots = '.' * DOTS_NUM
    result = ''
    if len(string) == LENGTH:
        return string
    elif len(string) > LENGTH:
        length_difference = len(string) - LENGTH
        subtractor = length_difference + DOTS_NUM
        result = string[:len(string) - subtractor] + dots
    elif len(string) < LENGTH:
        additional_space = ' ' * (LENGTH - len(string))
        result = string[:] + additional_space
    return result

def print_books(books: list[tuple]) -> None:
    lines: list = []
    for book in books:
        book_data_str = list(map(str, book))
        string = '   '.join(map(cut, book_data_str))
        lines.append(string)
    print_columns(spaces=10)
    print('\n'.join(lines))
