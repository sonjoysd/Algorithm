def subset_sum(arr, target_sum):
    """
    Determine if a subset of arr sums to target_sum.
    Time Complexity: O(n * sum)
    Space Complexity: O(sum)
    """
    n = len(arr)
    # dp[i] is True if sum i is achievable
    dp = [False] * (target_sum + 1)
    dp[0] = True  # sum of 0 is always possible (empty subset)
    
    for num in arr:
        # Traverse right to left to avoid using same element twice
        for i in range(target_sum, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target_sum]


# Example usage
if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    target = 9
    
    result = subset_sum(arr, target)
    print(f"Can achieve sum {target}: {result}")  # Output: True (4+5=9)