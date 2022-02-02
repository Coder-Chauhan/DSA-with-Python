def sum_of_array(arr):
    n = len(arr)
    if n == 0:
        return 0
    small_output = sum_of_array(arr[1:])
    return arr[0] + small_output
    
arr = [9,8,9,10]
print(sum_of_array(arr
