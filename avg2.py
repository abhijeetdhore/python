n=int(input("enter the np. of elements to insert:"))
l=[]
for i in range(0,n):
    element=int(input("enter element:"))
    avg=sum(l)/n
    l.append(element)
print("avarage=",avg)