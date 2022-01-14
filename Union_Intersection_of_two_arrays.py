def union(arr1,arr2):
    u = []
    for i in (arr1 and arr2):
        u.append(i)
    return print("The union of the two array is :", u)


def intersection(arr1,arr2):
    
    return list(set(arr1) & set(arr2))

n = int(input("Enter the length of the 1st array : "))
print("Enter the first array : ")
arr1 = []

for i in range(n):
    ele = int(input())
    arr1.append(ele)

m = int(input("Enter the length of the 2nd array : "))
print("Enter the second array : ")
arr2 = []

for i in range(m):
    ele = int(input())
    arr2.append(ele)

print("The first array is :", arr1)
print("The second array is :", arr2)
print(union(arr1,arr2))
print(intersection(arr1,arr2))