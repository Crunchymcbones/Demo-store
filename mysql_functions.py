import mysql.connector


def executeQueryAndReturnResult(query, host='localhost', username='root', password='root', port=3306, database='easy_cheese'):
    """
    Executes a given SQL query on the specified MySQL database and returns the result.

    Args:
    - query (str): The SQL query to be executed.
    - host (str): The hostname of the MySQL server. Default is 'localhost'.
    - username (str): The username to be used for authentication. Default is 'root'.
    - password (str): The password to be used for authentication. Default is 'root'.
    - port (int): The port number to be used for connecting to the MySQL server. Default is 3306.
    - database (str): The name of the MySQL database to be used. Default is 'easy_cheese'.

    Returns:
    - A tuple containing:
        - column_names (list): A list of column names returned by the query.
        - rows (list of tuples): A list of tuples, where each tuple represents a row returned by the query.
    """
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.column_names, cursor.fetchall()

def executeQueryAndCommit(query, host='localhost', username='root', password='root', port=3306, database='easy_cheese'):
    """
    Executes a given SQL query on the specified MySQL database and commits the changes.

    Args:
    - query (str): The SQL query to be executed.
    - host (str): The hostname of the MySQL server. Default is 'localhost'.
    - username (str): The username to be used for authentication. Default is 'root'.
    - password (str): The password to be used for authentication. Default is 'root'.
    - port (int): The port number to be used for connecting to the MySQL server. Default is 3306.
    - database (str): The name of the MySQL database to be used. Default is 'easy_cheese'.

    Returns:
    - The number of rows affected by the query.
    """
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount

