import mysql.connector


def executeQueryAndReturnResult(query, host='localhost', username='root', password='root', port=3306,
                                database='easy_cheese'):
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.column_names, cursor.fetchall()


def executeQueryAndCommit(query, host='localhost', username='root', password='root', port=3306, database='easy_cheese'):
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount
