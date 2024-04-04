n=int(input("Enter the number of terms:"))
sum=0
t=1
for i in range (1,n+1):
    sum=sum+(t*(-1)**i)
    t=t+2
print("sum=",sum)
    