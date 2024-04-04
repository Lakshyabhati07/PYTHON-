n=int(input("Enter the number of rows to print:"))
for i in range (1,n+1):
    for k in range (n,i+1):
        print(" ")
    for j in range ('A','A'+1):
        print(j)
    for j in range (j-2,'A'):
        print(j)
    print("/r")
    