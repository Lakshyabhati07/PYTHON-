for n in range(1,1001):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    if sum%n==0:
        print("\t",n,end="")