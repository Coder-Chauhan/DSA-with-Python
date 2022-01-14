def rotate(arr,n):
    last_element = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last_element
    return arr

n = int(input("Enter the len of the array : "))
print("Enter the array : ")
arr = []

for i in range(n) :
    ele = int(input())
    arr.append(ele)

print("The array is :", arr)
print("The rotated array is :", rotate(arr,n))