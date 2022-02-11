# fucntion for reversing the list
def reverse_array(li) :
    li.reverse()
    return li

n = int(input("Enter the length of the array : "))
print("Enter the list")
li = []

for i in range(n):
    ele = int(input())
    li.append(ele)

print(li)
print(reverse_
