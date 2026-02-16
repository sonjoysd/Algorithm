def radix_sort(arr):
    """
    Radix sort algorithm that sorts numbers by individual digits.
    Time complexity: O(d * n) where d is the number of digits
    """
    if not arr:
        return arr
    
    # Find the maximum number to know number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def counting_sort_by_digit(arr, exp):
    """
    Counting sort based on digit at position exp
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count[i] so it contains actual position
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy the output array to arr
    for i in range(n):
        arr[i] = output[i]


# Example usage
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 2, 802, 24, 2, 66]
    print("Original array:", arr)
    radix_sort(arr)
    print("Sorted array:", arr)