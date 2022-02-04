# Program to find the minimum and maximum number in an array
def min_max(li) :
    print("Maximum element is :", max(li))
    print("Minimum element is :", min(li))
    return

n = int(input("Enter the length of the array : "))
print("Enter the array")
li = []

for i in range(n):
    ele = int(input())
    li.append(ele)

print("List :", li)

