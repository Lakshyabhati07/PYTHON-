def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if(left[i]<=right[j]):
            result.append(left[i])
            i=i+1
        else:
            result[i].append(right[j])
            j=j+1
    result+=left[i:]
    result+=right[j:]
    return result

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)/2
    left=merge_sort(lst[:mid])
    right=merge_sort(lst[mid:])
    return merge(left,right)

arr=[1,2,3,0,9,8,-1]
print(merge_sort)