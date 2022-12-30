# leetcode.com/problems/two-sum
"""
덧셈하여 타겟을 만들 수 있느 ㄴ배열의 두 숫자 인덱스를 return 
"""

from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # 정답에서 해당 value 값을 뺀 엘리먼트가 nums에 있다면 그것은 정답
        # in 의 시간복잡도 O(n)
        for num, value in enumerate(nums): 
            least_num = target - value

            # 인덱스 앞까지 굳이 다시 체크할필요가 없으므로 인덱스 +1 번부터 체크
            if least_num in nums[num + 1:]:
                # 잔여 숫자에 index가 num+1 부터 시작해 0으로 초기화 되므로 나온 인덱스값에서 (num+1)만큼 더해준다
                return [nums.index(value), nums[num+ 1:].index(least_num) + (num + 1)]
 





solution=Solution()
answer = solution.twoSum2([11,2,15,7], 9)
#output -> [1, 3]
print(answer)