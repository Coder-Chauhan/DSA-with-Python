def print_1_to_n(n):
    if n==0:
        return   
    print(n)
    print_1_to_n(n-1)
    return

n = int(input())
print_1_to_n(n)