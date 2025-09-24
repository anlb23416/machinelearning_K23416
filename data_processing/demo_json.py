import pandas as pd
df=pd.read_json('../dataset/Sales_Transaction/SalesTransactions.json', encoding='utf-8', dtype='unicode')
print(df)