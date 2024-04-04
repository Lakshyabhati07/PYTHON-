#binary search ka function
#O(nlogn) time
#O(1) space
def binary_sear(a,low,high,x):
    if(high>=low):
        mid=(high+low)//2
    
        if(x==a[mid]):
            return mid
        elif x>a[mid]:
            return binary_sear(a,mid+1,high,x)
        else:
            return binary_sear(a,low,mid-1,x)
    else:
        return -1

#list ko input krne k liye
a=[]
size=int(input("Enter size of list:"))
for i in range(size):
    val=int(input("Enter the value:"))
    a.append(val)

#values dene k liye
low=0
high=size-1
x=int(input("Enter the value of key:"))
print(binary_sear(a,low,high,x))
