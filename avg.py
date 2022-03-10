a=int(input("enter test 1 m1rks="))
b=int(input("enter test 2 marks="))
c=int(input("enter test 3 marks="))
d=int(input("enter test 4 marks"))
A=a+b+c+d
print("addition=",A)
AVG=A/4
print("averag=",AVG)
testmarks=[a,b,c,d]
x=bytearray(testmarks)
for i in x:print(i)