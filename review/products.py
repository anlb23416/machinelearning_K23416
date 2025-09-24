class listProduct:
    def __init__(self):
        self.products=[]
    def add_product(self,p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)
    def desc_sort_products(self):
        for i in range(0, len(self.products)):
            for j in range(i+1, len(self.products)):
                pi=self.products[i]
                pj=self.products[j]
                if pi.price < pj.price:
                    self.products[j]=pi
                    self.products[i]=pj

    def desc_sort_product(self):
        return sorted(self.products, key=lambda p: p.price, reverse=True)
    def giam_dan(self):
        i=0
        while i < len(self.products) - 1:
            pw = self.products[i]
            pe = self.products[i + 1]

            if pw.price < pe.price:
                # hoán đổi
                self.products[i], self.products[i+1] = pe, pw
                # quay lại đầu danh sách
                i = 0
            else:
                i += 1