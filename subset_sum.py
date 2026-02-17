def subset_sum(nums, target):
    """
    Determine if there's a subset of nums that sums to target.
    Returns True if possible, False otherwise.
    """
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]


# Example usage
if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print(f"Subset sum exists: {subset_sum(nums, target)}")