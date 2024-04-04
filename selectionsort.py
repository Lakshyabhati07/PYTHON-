def selection_sort(a,size):
    for i in range(size):
        min_value=i
        for j in range(i,size+1):
            if a[j]<a[min_value]:
                min_value=j
        
        temp=a[i]
        a[i]=a[min_value]
        a[min_value]=temp

a=[]
size=int(input("Enter size of list:"))
for i in range(size):
    val=int(input("Enter the value:"))
    a.append(val)

selection_sort(a,size)
print(a)