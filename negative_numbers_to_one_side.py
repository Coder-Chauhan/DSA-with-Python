def rearrange(arr,n):
    j = 0
    for i in range(n):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j+=1
    return arr

n = int(input("Enter the length of the array : "))
print("Enter the elements : ")
arr = []

for i in range(n) :
    ele = int(input())
    arr.append(ele)

print(arr)
print(rearrange(arr,n)
