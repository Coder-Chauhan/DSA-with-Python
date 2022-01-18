def power_of_n(n,x):
    ans = 1
    while  n > 0:
        ans = ans*x
        n-=1
    return ans

n,x = input().split()
x = int(x)
n = int(n)
print(power_of_n(n,x))