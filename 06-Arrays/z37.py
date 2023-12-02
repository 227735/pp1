def second_largest(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[-2]

def difference_largest_smallest(arr):
    return max(arr) - min(arr)

def median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        mid1 = sorted_arr[n // 2 - 1]
        mid2 = sorted_arr[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_arr[n // 2]

def smallest_and_largest(arr):
    return [min(arr), max(arr)]

def array_as_string(arr):
    result = ''
    for num in arr:
        result += str(num) + '-'
    return result.rstrip('-')

numbers = [7, 3, 8, 5, 2]

print("Numbers:", ', '.join(str(num) for num in numbers))

print("Second largest number:", second_largest(numbers))
print("Median:", median(numbers))
print("Smallest and largest number:", ', '.join(map(str, smallest_and_largest(numbers))))
print("Numbers as a string:", array_as_string(numbers))