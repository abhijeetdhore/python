x=int(input("enter the price of product="))
y=int(input("enter the Quantity="))
z=x*y
print("Gross AMount=",z)

if z>=5000:
    dis=z*0.10;
    z=z-dis
    print("Discount=",dis)
    print("Net Amount=",z)
else:
    print("Net Amount=",z)

