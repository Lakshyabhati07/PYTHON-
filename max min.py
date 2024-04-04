n=int(input("Enter the total list of numbers:"))
for i in range(1,n+1):
    num=(int(input()))
    if i==1:
        min=num
        max=num
    else:
        if min>=num:
            min=num
        if max>=num:
            max=num
print("Minimum no. is:",min)
print("Maximum no. is:",max)