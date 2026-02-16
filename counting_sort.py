def counting_sort(arr):
    """
    Sorts an array of non-negative integers using counting sort.
    Time Complexity: O(n + k) where n is array length and k is range of input
    Space Complexity: O(k)
    """
    if not arr:
        return arr
    
    # Find the maximum element
    max_val = max(arr)
    min_val = min(arr)
    
    # Handle negative numbers by shifting
    range_size = max_val - min_val + 1
    count = [0] * range_size
    
    # Count occurrences of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Modify count array to contain cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):
        index = num - min_val
        output[count[index] - 1] = num
        count[index] -= 1
    
    return output


# Example usage
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Original array:", arr)
    print("Sorted array:", counting_sort(arr))