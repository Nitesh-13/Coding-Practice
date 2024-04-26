# TCS NQT 2024 26 April Slot 2

'''
'xyz' sales company have the sales record in format of tuples. Each tuple contains product name, product unit price, product sold count. You need to count the total sale, average sale and the most selling product.
Note: Decimal place round off to 2 is compulsory 

Example 1:
Input:
[('apple',10.0,5),('orange',5.0,10),('apple',1.0,5)]
Output:
Total Sale: 105.00
Average Sale: 35.00
Most Selling Product: apple

Example 2:
Input:
[('apple',10.0,10),('banana',0.5,15),('apple',6.0,12),('orange',0.8,15),('banana',5.0,20),('orange',9.0,15)]
Output:
Total Sale: 426.50
Average Sale: 71.08
Most Selling Product: banana

'''

inp=eval(input())
total = 0.00
sales = {}

for tupl in inp:
    sales.setdefault(tupl[0], 0)
    sales[tupl[0]] += tupl[2]
    total += (tupl[2]*tupl[1])
maxSale = 0
maxSaleItem = ''
for key, value in sales.items():
    if maxSale < value:
        maxSale = value
        maxSaleItem = key


print("{:.2f}".format(total))
print("{:.2f}".format(total/len(inp)))
print(maxSaleItem)