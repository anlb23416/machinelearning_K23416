import sqlite3
import pandas as pd

def top_n_customers(n):
    try:
        sqliteConnection = sqlite3.connect('../database/databases/databases/Chinook_Sqlite.sqlite')
        query = f"""
            SELECT c.CustomerId, 
                   c.FirstName || ' ' || c.LastName AS CustomerName,
                   COUNT(DISTINCT i.InvoiceId) AS InvoiceCount,
                   SUM(il.Quantity * il.UnitPrice) AS TotalContribution,
                   ROUND(AVG(il.Quantity * il.UnitPrice), 2) AS AvgLineValue
            FROM Customer c
            JOIN Invoice i ON c.CustomerId = i.CustomerId
            JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
            GROUP BY c.CustomerId
            ORDER BY TotalContribution DESC
            LIMIT {n};
        """
        # Trả về DataFrame
        df = pd.read_sql_query(query, sqliteConnection)
        return df

    except sqlite3.Error as error:
        print("Error occurred -", error)
        return None
    finally:
        if sqliteConnection:
            sqliteConnection.close()

n = int(input("Vui lòng nhập số lượng khách hàng top n: "))
df = top_n_customers(n)
print(df)