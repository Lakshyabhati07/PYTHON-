n=int(input("Enter the number of rows to print:"))
for i in range (0,n):
    for j in range (0,n):
        if((i+j)%2==0):
            print("1",end="")
        else:
            print("0",end="")
    print("\r")