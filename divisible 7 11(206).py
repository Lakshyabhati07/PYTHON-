n=100
sum=0
print("NO. divisible by 7 is:")
while(n<=200):
    if n%7==0:
        print("\t",n,end="")
        sum=sum+n
    n=n+1

print("\nsum=",sum)