#gcd recursion
# dono m se jo 0 hoga uska ulta
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
print(gcd(a,b))
