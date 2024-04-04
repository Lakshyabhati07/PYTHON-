#factorial recursion
# n=4 4*3*2*1 (1 p rukna h)
def fact(n):
    if n<=0:
        print("Invalid number")
    if n==1:
        return 1
    else:
        return (fact(n-1)*n)

n=int(input("Enter the number:"))
print(fact(n))