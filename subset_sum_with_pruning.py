def subset_sum_with_pruning(arr, target):
    """
    Find all subsets that sum to the target value using backtracking with pruning.
    
    Args:
        arr: List of integers
        target: Target sum value
    
    Returns:
        List of subsets that sum to target
    """
    arr.sort()  # Sort to enable pruning
    result = []
    
    def backtrack(start, current_subset, current_sum):
        # Base case: if sum equals target, add to result
        if current_sum == target:
            result.append(current_subset[:])
            return
        
        # Pruning: if current sum exceeds target, stop
        if current_sum > target:
            return
        
        for i in range(start, len(arr)):
            # Pruning: if adding current element exceeds target, skip remaining
            if current_sum + arr[i] > target:
                break
            
            # Include current element
            current_subset.append(arr[i])
            backtrack(i + 1, current_subset, current_sum + arr[i])
            current_subset.pop()  # Backtrack
    
    backtrack(0, [], 0)
    return result


# Example usage
if __name__ == "__main__":
    numbers = [3, 34, 4, 12, 5, 2]
    target = 9
    
    subsets = subset_sum_with_pruning(numbers, target)
    print(f"Subsets that sum to {target}:")
    for subset in subsets:
        print(subset)