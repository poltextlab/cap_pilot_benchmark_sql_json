import config
import mysql.connector

HOST = config.HOST
USER = config.USER
PASSWORD = config.PASSWORD
DATABASE_NAME = config.DATABASE


def start(debug=False) -> None:
    """
    Method to create the working database.

    :return: None
    """

    # Initialize the database
    __init_database(host=HOST, user=USER, password=PASSWORD, name=DATABASE_NAME, debug=debug)


def get_database_reference():
    return __get_connection(host=HOST, user=USER, password=PASSWORD, database=DATABASE_NAME)


def check_tables() -> None:
    """
    Prints to standard output the names of already existing tables in database.

    :return: None
    """

    cursor, db = __get_connection(host=HOST, user=USER, password=PASSWORD, database=DATABASE_NAME)
    try:
        cursor.execute(f"SHOW TABLES FROM {db}")
        for x in cursor:
            print(x)
        __close_connection(cursor, db)
    except mysql.connector.Error as err:
        print('Error occured at {}'.format(__name__))
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def execute_insert(stmt: str, val: tuple) -> None:
    """
    Execute insertion with "prepared statement" (SQL injection protected)

    :param stmt: statement, where '%s' indicates the variables in the SQL expression
    :param val: tuple containing variables to replace in stmt parameter
    :return:
    """

    cursor, db = __get_connection(host=HOST, user=USER, password=PASSWORD, database=DATABASE_NAME)
    try:
        cursor.execute(stmt, val)
        db.commit()
        # print(cursor.rowcount, "record inserted.")
    except mysql.connector.Error as err:
        print('Error occured at {}'.format(__name__))
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def execute_statement(statement: str) -> None:
    """
    Function to create a table (specified by the parameter str) in the database (specified in the config.py
    file as DATABASE_NAME).

    :param statement: SQL statement to be performed, given in str
    :return: None
    """

    cursor, db = __get_connection(host=HOST, user=USER, password=PASSWORD, database=DATABASE_NAME)
    try:
        cursor.execute(statement)
        db.commit()
        __close_connection(cursor, db)

    except mysql.connector.Error as err:
        print('Error occured at {}'.format(__name__))
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def delete_database(debug=False) -> None:
    """
    Deletes a database.

    :param debug: If True, prints the existing databases if succeed
    :return: None
    """

    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    cursor = mydb.cursor()
    cursor.execute(f"DROP SCHEMA IF EXISTS {DATABASE_NAME}")
    if debug:
        cursor.execute("SHOW DATABASES")
        for x in cursor:
            print(x)
    __close_connection(cursor, mydb)


def create_database(cursor,
                    name: str,
                    debug=False) -> None:
    """
    Creates a new database with the use of mysql.connector

    :param cursor: Cursor for MySQL client
    :param name: Expected name of created database
    :param debug: If True, prints the existing databases if succeed
    :return:
    """

    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(name))
    if debug:
        cursor.execute("SHOW DATABASES")
        for x in cursor:
            print(x)
    cursor.close()


def __init_database(host: str,
                    user: str,
                    password: str,
                    name: str,
                    debug=False) -> None:
    """
    Private method that actually creates a database at the beginning of the working progress.

    :param host: Host name
    :param user: Username already set in MySQL
    :param password: Password for the given user
    :param name: Name of the database to create
    :param debug: If True, prints the existing databases
    :return: None
    """

    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        mycursor = mydb.cursor()
        create_database(mycursor, name, debug)
        __close_connection(mycursor, mydb)
    except mysql.connector.Error as err:
        print('Error occured at {}'.format(__name__))
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def __get_connection(host: str,
                     user: str,
                     password: str,
                     database: str) -> tuple:
    """
    Private method that gets reference for a database and a Cursor object for it

    :param host: Host name
    :param user: Username already set in MySQL
    :param password: Password for the given user
    :param database: For getting a reference and a Cursor object
    :return: Tuple: (Cursor, Database)
    """

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = mydb.cursor()
    return cursor, mydb


def __close_connection(mycursor,
                       mydb) -> None:
    """
    Private method that closes the connection with a given database.

    :param mycursor: Cursor for the database
    :param mydb: reference to the opened databse (MySQL)
    :return: None
    """
    mycursor.close()
    mydb.close()
