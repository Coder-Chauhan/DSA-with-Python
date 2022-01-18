def fib(n):
    if n == 2 or n==1:
        return 1
    fib_n_1 = fib(n-1)
    fib_n_2 = fib(n-2)
    output = fib_n_1 + fib_n_2
    return output

n = int(input())
print(fib(n))