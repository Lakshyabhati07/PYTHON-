n=int(input("enter the no. of terms:"))
pre=1
cur=1
while(cur<n):
    print(pre*cur,"\t",end="")
    pre=cur
    cur+=1
    