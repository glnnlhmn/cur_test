import sqlite3


def con_not_closed():

    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        # cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        # if sqliteConnection:
            #sqliteConnection.close()
        print("The SQLite connection not closed")


def con_not_closed_2():
    con_not_closed()
    print("Left function")