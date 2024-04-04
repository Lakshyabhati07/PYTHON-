#fibbonacci recursion
#0 1 1 2 3 5..
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fib(n-1)+fib(n-2))

n=int(input("enter the number of terms: "))
for i in range(1,n+1):
    print(fib(i),end=" ")