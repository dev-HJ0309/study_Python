import pymysql

from pymysql.cursors import Cursor


def connect():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='app', charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor


def execute_crud(execute):
    result = None
    # 이렇게 써야 외부에 있는 것을 수정 할 수 있다 1

    def manage(*args):
        nonlocal result
        # 이렇게 써야 외부에 있는 것을 수정 할 수 있다 2
        conn, cursor = connect()

        try:
            result = execute(cursor, *args)
            conn.commit()
        except Exception as e:
            print(e.__str__())
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

        return result

    return manage


@execute_crud
def save(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)


@execute_crud
def find_all(cursor: Cursor, query: str):
    cursor.execute(query)
    return cursor.fetchall()


@execute_crud
def update(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)


@execute_crud
def delete(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)


@execute_crud
def find_by_id(cursor: Cursor, query: str):
    cursor.execute(query)
    return cursor.fetchone()

@execute_crud
def find_by_member_id(cursor: Cursor, query: list):
    cursor.execute(query)
    return cursor.fetchone()






