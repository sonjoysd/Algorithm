from typing import List, Tuple

def subset_sum_backtracking(nums: List[int], target: int) -> List[List[int]]:
    result: List[List[int]] = []
    nums.sort()

    def backtrack(start: int, current: List[int], total: int) -> None:
        if total == target:
            result.append(current.copy())
            return
        if total > target:
            return
        prev = None
        for i in range(start, len(nums)):
            if prev is not None and nums[i] == prev:
                continue
            current.append(nums[i])
            backtrack(i + 1, current, total + nums[i])
            current.pop()
            prev = nums[i]

    backtrack(0, [], 0)
    return result


if __name__ == "__main__":
    data = [3, 1, 2, 5, 1, 4]
    target_sum = 6
    solutions = subset_sum_backtracking(data, target_sum)
    print("Solutions:", solutions)