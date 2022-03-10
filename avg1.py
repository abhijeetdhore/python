n=int(input("Enter the no.of eliments to be inserted:"))
a=[]
for i in range(0,n):
    element=int(input("enter element:"))
    a.append(element)
avg=sum(a)/n
print("avarage",avg)