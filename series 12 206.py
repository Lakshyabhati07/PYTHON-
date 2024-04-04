terms=int(input("enter no. of terms:" ))
n=1
count=1
while (count<=terms):
    if count%2==0:
        n=n+3
    else:
        n+=1
    print(n,"\t",end="")
    count+=1
    