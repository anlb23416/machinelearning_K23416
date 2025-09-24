import pandas as pd

df = pd.read_csv('../dataset/Sales_Transaction/SalesTransactions.csv')

def top_3_product_sales(df):
    # Tạo cột Sales_Value = Quantity * UnitPrice * (1 - Discount)
    df['Sales_Value'] = df['Quantity'] * df['UnitPrice'] * (1 - df['Discount'])

    # Tính tổng doanh số theo OrderID
    total_orders = df.groupby('ProductID')['Sales_Value'].sum()

    # Lấy top 3 đơn hàng có tổng doanh số cao nhất
    top_3_products = total_orders.sort_values(ascending=False).head(3)

    return top_3_products.to_dict()

result = top_3_product_sales(df)

print('Top 3 sản phẩm bán chạy nhất:')
for order_id, value in result.items():
    print(f"Đơn hàng {order_id} có tổng giá trị: {value}")
