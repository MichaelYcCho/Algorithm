from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    memo = {}
    for k, v in enumerate(nums):
        if target - v in memo:
            return [memo[target - v], k]
        memo[v] = k


two_sum(nums=[4, 1, 9, 7, 5, 3, 16], target=14)
