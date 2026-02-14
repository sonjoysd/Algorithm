def hash_sort(arr):
    """
    Hash sort algorithm - distributes elements into buckets based on hash values,
    then concatenates sorted buckets.
    """
    if not arr:
        return arr
    
    # Find min and max for range
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    
    # Create buckets
    buckets = [[] for _ in range(range_size)]
    
    # Distribute elements into buckets
    for num in arr:
        index = num - min_val
        buckets[index].append(num)
    
    # Concatenate all buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr


# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    print(f"Sorted: {hash_sort(arr)}")