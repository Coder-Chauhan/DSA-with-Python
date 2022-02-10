# Program to find the kth minimum and maximum number in an array
def min_max(li,k,n) :
    li.sort()
    print(f"{k}th Maximum element is :", li[n-k-1])
    print(f"{k}th Minimum element is :", li[k-1])
    return

n = int(input("Enter the length of the array : "))
print("Enter the array")
li = []

for i in range(n):
    ele = int(input())
    li.append(ele)

k = int(input("Enter the kth number"))

print("List :", li)
print(m
