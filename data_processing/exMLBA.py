import pandas as pd

df=pd.read_csv('../dataset/Sales_Transaction/SalesTransactions.csv')

print(df)
def find_orders_within_range(df,minValue,maxValue):
    #Total of orders
    orders_total = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    )

    #lọc danh sách đơn hàng trong range
    orders_within_range = orders_total[(orders_total >= minValue) & (orders_total <= maxValue)]
    #Danh sách đơn hàng không trùng nhau
    unique_orders=df[df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().tolist()
    if unique_orders == sorted(unique_orders):
        SortType = True
    else:
        SortType = False
    return unique_orders, SortType

minValue=float(input("Nhập giá trị min: "))
maxValue=float(input("Nhập giá trị max: "))
result,SortType=find_orders_within_range(df,minValue,maxValue)
print('Danh sách các hóa đơn trong phạm vi giá trị từ',minValue,'đến',maxValue, 'là', result)
print('Thứ tự của danh sách là', SortType)