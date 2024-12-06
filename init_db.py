import sqlite3
from config import DB_NAME


def init_db(db_name: str) -> None:
    try:
        with sqlite3.connect(database=db_name) as conn:
            curs = conn.cursor()
            curs.execute('''
                        CREATE TABLE books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            author TEXT,
                            year INTEGER,
                            status TEXT DEFAULT "в наличии"
                        )
                        ''')
        print(f'База данных "{DB_NAME}" успешно создана')
    
    except sqlite3.Error as e:
        print(f'Ошибка базы данных: {e}')
        

if __name__ == '__main__':
    init_db(db_name=DB_NAME)
