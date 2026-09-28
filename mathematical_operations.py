def factorial_number(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i

    return result
def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result
import math

def square_root(n):
    return math.sqrt(n)
def base_conversion(decimal, base):
    number = decimal
    result = ""

    while number > 0:
        remainder = number % base

        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(55 + remainder) + result

        number = number // base

    return result
print(factorial_number(5))
print(base_conversion(25, 2))
