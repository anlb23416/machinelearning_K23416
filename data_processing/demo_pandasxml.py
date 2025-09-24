import pandas_read_xml as pdx

df=pdx.read_xml('../dataset/Sales_Transaction/SalesTransactions.xml',['UelSample','SalesItem'])

print(df.iloc[0]) #in toàn bộ data
data=df.iloc[0]
print(data[0]) #In ra dòng đầu tiên
print(data[1])
print(data[1]['OrderID'])
