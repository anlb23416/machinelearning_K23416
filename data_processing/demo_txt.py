import pandas as pd

df=pd.read_csv("../dataset/Sales_Transaction/SalesTransactions.txt", sep="\t",
               low_memory=False,
               encoding='utf-8',
               dtype='unicode')
#Cái sep="\t" là dùng để chuyển thành tiếng việt. Kiểu khi print ra thì nó bị còn dấu \ đọc ko được thì cái đó đọc đưc
print(df.head())
print(df[df['UnitPrice']>30])
