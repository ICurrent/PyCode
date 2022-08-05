def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
for i in range(n):
    print(fibonacci(i))