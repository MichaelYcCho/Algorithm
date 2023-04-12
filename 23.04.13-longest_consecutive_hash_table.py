# https://leetcode.com/problems/longest-consecutive-sequence/submissions/933064203/

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    longest = 0
    num_dict = {}
    for num in nums:
        num_dict[num] = True

    for num in num_dict:
        # 중복 탐색을 막기 위해, 앞의 수가 없는 경우만 탐색
        if num - 1 not in num_dict:
            cnt = 1
            target = num + 1
            # 연속된 수를 찾기 위해, 뒤의 수가 있는 경우만 탐색
            while target in num_dict:
                cnt += 1
                target += 1
            longest = max(longest, cnt)

    return longest


print(longest_consecutive(nums=[100, 4, 200, 1, 3, 2]))


def longest_consecutive_set(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    max_val = 1
    num_set = set(nums)
    for x in num_set:
        if x - 1 not in num_set:
            val = 1
            target = x + 1
            while target in num_set:
                val += 1
                target += 1
            max_val = max(max_val, val)

    return max_val


print(longest_consecutive_set(nums=[100, 4, 200, 1, 3, 2]))
