def liner_se(a,size,x):
    for i in range(size):
        if a[i]==x:
            return i
    
    return -1

def lin(a,size,x):
    if size==0:
        return -1
    elif x==a[size-1]:
        return size-1
    else:
        return lin(a,size-1,x)
a=[]
size=int(input("Enter size of list:"))
for i in range(size):
    val=int(input("Enter the value:"))
    a.append(val)
x=int(input("Enter the value of key:"))
print(lin(a,size,x))