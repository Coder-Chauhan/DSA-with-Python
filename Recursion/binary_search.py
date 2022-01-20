def binary_search(a,x,si,ei):
    f si > ei:
        return -1
    mid = (si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid] > x:
        return binary_search(a,x,si,mid-1)
    else :
        return binary_search(a,x,mid+1,ei)
a = [1,2,3,4,5,6,7,8]
print(binary_search(a,4,0,7))
