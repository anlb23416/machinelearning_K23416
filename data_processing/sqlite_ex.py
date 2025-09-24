import sqlite3

import pandas as pd
try:
    sqliteConnecttion=sqlite3.connect('../database/databases/databases/Chinook_Sqlite.sqlite')
    cursor=sqliteConnecttion.cursor()
    print('DB Init')

    query='SELECT * FROM InvoiceLine LIMIT 5;'
    cursor.execute(query)

    df=pd.DataFrame(cursor.fetchall())
    print(df)

    cursor.close()
except sqlite3.Error as error:
    print('Error occured - ', error)
finally:
    if sqliteConnecttion:
        sqliteConnecttion.close()
        print('SQLite Connection closed')