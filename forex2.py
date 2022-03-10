#wap to print multiplication table of 1 to 5
i=1
j=5
for i in range(1, 11):
    for j in range(1,6):
        print('{:8}'.format(i*j), end='')
    print()