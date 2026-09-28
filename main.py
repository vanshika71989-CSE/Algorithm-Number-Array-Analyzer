from number_analysis import *
from array_analysis import *
from mathematical_operations import *

while True:
    print("\n===== Algorithm-Based Number & Array Analysis System =====")
    print("1. Number Analysis")
    print("2. Array Analysis")
    print("3. Mathematical & Conversion Operations")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n===== Number Analysis =====")
        print("1. Prime Number")
        print("2. GCD")
        print("3. Prime Factorization")
        print("4. Smallest Divisor")
        print("5. Palindrome")
        print("6. Fibonacci")
        print("7. Back to Main Menu")

        number_choice = int(input("Enter your choice: "))

        if number_choice == 1:
            n = int(input("Enter a number: "))

            if prime_number(n):
                print("Prime Number")
            else:
                print("Not a Prime Number")

        elif number_choice == 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            print("GCD =", gcd(a, b))

        elif number_choice == 3:
            n = int(input("Enter a number: "))

            print("Prime Factors:")
            prime_factors(n)

        elif number_choice == 4:
            n = int(input("Enter a number: "))

            print("Smallest Divisor =", smallest_divisor(n))

        elif number_choice == 5:
            n = int(input("Enter a number: "))

            if palindrome(n):
                print("Palindrome")
            else:
                print("Not a Palindrome")

        elif number_choice == 6:
            n = int(input("Enter the number of terms: "))

            print("Fibonacci Series =", fibonacci(n))

        elif number_choice == 7:
            print("Returning to Main Menu")

        else:
            print("Invalid Choice")

    elif choice == 2:
        print("\n===== Array Analysis =====")
        print("1. Maximum Element")
        print("2. Reverse Array")
        print("3. Count Elements")
        print("4. Remove Duplicates")
        print("5. Kth Smallest Element")
        print("6. Back to Main Menu")

        array_choice = int(input("Enter your choice: "))

        if array_choice == 1:
            arr = list(map(int, input("Enter array elements: ").split()))
            print("Maximum Element =", maximum_element(arr))

        elif array_choice == 2:
            arr = list(map(int, input("Enter array elements: ").split()))
            print("Reversed Array =", reverse_array(arr))

        elif array_choice == 3:
            arr = list(map(int, input("Enter array elements: ").split()))
            print("Number of Elements =", count_elements(arr))

        elif array_choice == 4:
            arr = list(map(int, input("Enter array elements: ").split()))
            print("Array after removing duplicates =", remove_duplicates(arr))

        elif array_choice == 5:
            arr = list(map(int, input("Enter array elements: ").split()))
            k = int(input("Enter the value of K: "))

            print("Kth Smallest Element =", kth_smallest(arr, k))

        elif array_choice == 6:
            print("Returning to Main Menu")

        else:
            print("Invalid Choice")

    elif choice == 3:
        print("\n===== Mathematical & Conversion Operations =====")
        print("1. Factorial")
        print("2. Power")
        print("3. Square Root")
        print("4. Base Conversion")
        print("5. Back to Main Menu")

        math_choice = int(input("Enter your choice: "))

        if math_choice == 1:
            n = int(input("Enter a number: "))
            print("Factorial =", factorial_number(n))

        elif math_choice == 2:
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))

            print("Power =", power(base, exponent))

        elif math_choice == 3:
            n = float(input("Enter a number: "))
            print("Square Root =", square_root(n))

        elif math_choice == 4:
            decimal = int(input("Enter a decimal number: "))
            base = int(input("Enter the base: "))

            print("Converted Number =", base_conversion(decimal, base))

        elif math_choice == 5:
            print("Returning to Main Menu")

        else:
            print("Invalid Choice")

    elif choice == 4:
        print("Thank you for using the system!")
        break

    else:
        print("Invalid Choice")
        