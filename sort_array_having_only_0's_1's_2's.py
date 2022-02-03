def sort(li,n):
    sorted_li = []
    zero_count = 0
    one_count = 0
    two_count = 0
    for i in li:
        if i == 0:
            zero_count+=1
        elif i == 1:
            one_count+=1
        else :
            two_count+=1

    for i in range(zero_count):
        sorted_li.append(i)
    for i in range(one_count):
        sorted_li.append(i)
    for i in range(two_count):
        sorted_li.append(i)

    return sorted_li        

print("running")
n = int(input("Enter the length of the array : "))
li = []

for i in range(n):
    ele = int(input())
    li.append(ele)

print("List :", li)
print("Sorted List :", sort(li,n))
