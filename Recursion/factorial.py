def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else :
        return 1

n = int(input("Enter the nth number :"))
print(factorial(n)
