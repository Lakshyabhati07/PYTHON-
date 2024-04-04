def swap(x,y):
    
    x,y = y,x
    
    return x,y
#swap
a=int(input("enter the a:  "))
b=int(input("enter the b:  "))

a,b=swap(a,b)
print("A IS",a)
print(b)