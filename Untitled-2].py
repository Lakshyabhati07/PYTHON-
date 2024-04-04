#LCM of two numbers:
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
a=x
b=y
while a!=b:
    if a<b:
        a=a+x
    else:
        b=b+y
print("LCM is ",a)