def sum_digit(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digit(n // 10)

n = int(input("Enter a number: "))
print("Sum of digits is", sum_digit(n))
