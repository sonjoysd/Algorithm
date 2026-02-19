def backtracking_with_pruning(candidates, target):
    """
    Find all combinations of candidates that sum to target using backtracking with pruning.
    
    Args:
        candidates: List of integers
        target: Target sum
    
    Returns:
        List of combinations that sum to target
    """
    result = []
    candidates.sort()  # Sort for pruning optimization
    
    def backtrack(start, path, remaining):
        # Base case: if remaining sum is 0, we found a valid combination
        if remaining == 0:
            result.append(path[:])
            return
        
        # Pruning: if remaining is negative, stop exploring this branch
        if remaining < 0:
            return
        
        # Explore all candidates starting from 'start'
        for i in range(start, len(candidates)):
            num = candidates[i]
            
            # Pruning: if current number exceeds remaining, stop
            # (since list is sorted, all further numbers will too)
            if num > remaining:
                break
            
            # Choose
            path.append(num)
            
            # Explore: allow reusing the same number (start=i)
            backtrack(i, path, remaining - num)
            
            # Unchoose
            path.pop()
    
    backtrack(0, [], target)
    return result


# Example usage
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    
    combinations = backtracking_with_pruning(candidates, target)
    print(f"Combinations that sum to {target}:")
    for combo in combinations:
        print(combo)