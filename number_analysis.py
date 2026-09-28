def prime_number(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a
def prime_factors(n):
    i = 2

    while n > 1:
        if n % i == 0:
            print(i, end=" ")
            n = n // i
        else:
            i = i + 1
def smallest_divisor(n):
    i = 2

    while n % i != 0:
        i = i + 1

    return i
def palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse == original
def fibonacci(n):
    first = 0
    second = 1
    series = []

    for i in range(n):
        series.append(first)
        next_term = first + second
        first = second
        second = next_term

    return series
print(prime_number(17))
print(gcd(12, 18))
print(palindrome(121))
