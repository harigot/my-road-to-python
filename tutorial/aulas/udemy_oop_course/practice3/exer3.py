'''
In the following class SalesPerson, add two class variables named total_revenue and names. 
The variable names should be a list that contains names of all salespersons and total_revenue 
should contain the total sales amount of all the salespersons. 
'''



class SalesPerson:
    total_revenue = 0
    names = []
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)


    def make_sale(self,money):
        self.sales_amount += money
        SalesPerson.total_revenue += money
 
    def __str__(self):
        return f'name: {self.name}, age: {self.age}, sale: {self.sales_amount}'


s1 = SalesPerson('Bob', 25)
s2 = SalesPerson('Ted', 22)
s3 = SalesPerson('Jack', 27)

s1.make_sale(1000)
s1.make_sale(1200)
s2.make_sale(5000)
s3.make_sale(3000)
s3.make_sale(8000)

print(s1)
print(s2)
print(s3)

print(SalesPerson.names)
print(SalesPerson.total_revenue)
