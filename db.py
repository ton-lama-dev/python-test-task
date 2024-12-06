import sqlite3
from config import DB_NAME


def add_book(title: str, author: str, year: str) -> None:
    with sqlite3.connect(database=DB_NAME) as conn:
        curs = conn.cursor()
        curs.execute('''
                    INSERT INTO books (title, author, year)
                    VALUES (?, ?, ?)
                    ''', (title, author, year))


def delete_book(id: int) -> None:
    with sqlite3.connect(database=DB_NAME) as conn:
        curs = conn.cursor()
        curs.execute('''
                    DELETE FROM books WHERE id = ?
                    ''', (id, ))
        if curs.rowcount == 0:
            raise ValueError(f'Книга с id {id} не существует.')


def search_books(key) -> list[tuple]:
    with sqlite3.connect(database=DB_NAME) as conn:
        curs = conn.cursor()
        curs.execute('''
                    SELECT * FROM books WHERE title = ? OR author = ? OR year = ?
                    ''', (key, key, key))
        data = curs.fetchall()
        return data
    

def get_all_books() -> list[tuple]:
    with sqlite3.connect(database=DB_NAME) as conn:
        curs = conn.cursor()
        curs.execute('''
                    SELECT * FROM books
                    ''')
        data = curs.fetchall()
        return data    


def change_book_status(id: int, new_status: str) -> None:
    with sqlite3.connect(database=DB_NAME) as conn:
        curs = conn.cursor()
        curs.execute('''
                    UPDATE books SET status = ? WHERE id = ?
                    ''', (new_status, id))
        if curs.rowcount == 0:
            raise ValueError(f'Книга с id {id} не существует.')
