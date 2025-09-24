from review.product import Product
from review.products import listProduct

lp=listProduct()
lp.add_product(Product(100,1,200,10))
lp.add_product(Product(300,3,12,60))
lp.add_product(Product(200,2,5,30))
lp.add_product(Product(400,5,53,120))
lp.add_product(Product(500,6,94,124))
print('List of Products: ')
lp.print_products()
#Sắp xếp sản phẩm theo đơn giá giảm dần
print('List of Products after descending sort: ')
lp.desc_sort_products()
lp.print_products()

print('test')
lp.desc_sort_product()
lp.print_products()

print('hehe')
lp.giam_dan()
lp.print_products()
