# conditional statement 2
item=(input("Enter the name of item: "))
quantity=int(input("Enter the number of item: "))
price=int(input("enter the price of one item: "))

sub_total=(quantity*price)
print(sub_total)
gst=(sub_total*5)
print(gst) 
amount = (sub_total+gst)
print(amount)

if amount >= 1000:
    discount=10
print(amount/10)
if amount < 1000:
    discount=5
print(amount/5)

