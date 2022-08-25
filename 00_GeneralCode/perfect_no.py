def perfectNumber(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

if __name__ == "__main__":
    n = int(input("Enter a number to check: "))
    print(perfectNumber(n))    