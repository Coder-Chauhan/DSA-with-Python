def sumOfN(n):
    if n == 1:
        return 1
    return n + sumOfN(n-1)

n = int(input("Enter the number : "))
print(sumOfN(n))