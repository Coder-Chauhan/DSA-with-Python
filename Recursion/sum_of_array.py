def sum_of_array(arr,n):
    if n == 0:
        return 0
    return arr[n]+sum_of_array(arr,n-1)
    
arr = [1,2,3,4,5,6]
n = len(arr)-1
print(sum_of_array(arr,n)+arr[0])