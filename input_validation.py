def is_positive_number(n):
    if n > 0:
        return True
    else:
        return False
def is_valid_choice(choice, minimum, maximum):
    if minimum <= choice <= maximum:
        return True
    else:
        return False
def is_non_negative_number(n):
    if n >= 0:
        return True
    else:
        return False
def is_valid_base(base):
    if 2 <= base <= 36:
        return True
    else:
        return False
