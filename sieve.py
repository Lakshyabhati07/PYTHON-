# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def sieve(n):
    prime=[]
    for i in range(n+1):
        prime.append(i)
    prime[0]=prime[1]=0
    p=2
    while(p*p<=n):
        if(p!=0):
            for i in range(p*2,n+1,p):
                prime[i]=0
        p=p+1
    for i in prime:
        if(prime[i]!=0):
            print(prime[i],end=" ")
            
rane=int(input())
sieve(rane)
