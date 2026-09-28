from number_analysis import prime_number

def test_prime_number():
    assert prime_number(17) == True
    assert prime_number(10) == False
from number_analysis import gcd

def test_gcd():
    assert gcd(12, 18) == 6
    assert gcd(20, 8) == 4
from array_analysis import maximum_element

def test_maximum_element():
    assert maximum_element([4, 8, 2, 6]) == 8
    assert maximum_element([10, 5, 7]) == 10
from array_analysis import kth_smallest

def test_kth_smallest():
    assert kth_smallest([7, 2, 9, 4, 1], 3) == 4
    assert kth_smallest([10, 5, 8, 2], 2) == 5
from mathematical_operations import factorial_number

def test_factorial():
    assert factorial_number(5) == 120
    assert factorial_number(4) == 24
from mathematical_operations import base_conversion

def test_base_conversion():
    assert base_conversion(25, 2) == "11001"
test_prime_number()
test_gcd()
test_maximum_element()
test_kth_smallest()
test_factorial()
test_base_conversion()

print("All test cases passed successfully!")