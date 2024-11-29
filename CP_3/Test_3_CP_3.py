import sqlite3
import pytest

@pytest.fixture(scope="module")
def db_connection():
    with sqlite3.connect(':memory:') as conn:
        cursor = conn.cursor()
        print('Database connection established')
        yield conn, cursor




def test_insert(db_connection):
    conn, cursor = db_connection
    cursor.execute('''create table if not exists test(ID_test int, datas varchar)''')
    cursor.execute('''INSERT  INTO test(ID_test, datas)values(1,'sassd')''')
    conn.commit()
    cursor.execute('''select * from test''')
    result = cursor.fetchall()
    print(result)
    assert result == [(1, 'sassd')]



def test_del(db_connection):
    conn, cursor = db_connection
    cursor.execute('''create table if not exists test(ID_test int, datas varchar)''')
    cursor.execute('''INSERT  INTO test(ID_test, datas)values(1,'sassd')''')
    conn.commit()

    cursor.execute('''delete from test''')
    conn.commit()
    cursor.execute('''select count(*) from test''')
    result = cursor.fetchall()
    assert result[0][0] == 0
