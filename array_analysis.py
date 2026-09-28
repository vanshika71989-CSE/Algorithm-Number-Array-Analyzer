def maximum_element(arr):
    max_element = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]

    return max_element
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1

    return arr
def count_elements(arr):
    count = 0

    for i in range(len(arr)):
        count = count + 1

    return count
def remove_duplicates(arr):
    unique = []

    for i in range(len(arr)):
        if arr[i] not in unique:
            unique.append(arr[i])

    return unique
def kth_smallest(arr, k):
    arr.sort()

    return arr[k - 1]
print(maximum_element([4, 8, 2, 6]))
print(kth_smallest([7, 2, 9, 4, 1], 3))
