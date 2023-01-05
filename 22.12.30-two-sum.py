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

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        # twoSum2에서 시간복잡도를 개선해보자
        # in 의 시간복잡도 O(n)

        hash_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for num, value in enumerate(nums): 
            hash_map[value] = num # {11: 0, 2: 1, 15: 2, 7: 3}

        
        # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
        for key, value in enumerate(nums):
            least_num = target - value
            # least_num의 key값은 hash_map 에 포함되어야하며, 
            # 해당 key는 중복사용을 막기위해 현재 key와 같지 않은지 확인해야 한다. 
            if least_num in hash_map and key != hash_map[least_num]:
                return [key, hash_map[least_num]]

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        # twoSum3에서 2번 사용한 for문을 1번으로 줄여보자
        for index, value in enumerate(nums):
            if target - value in hash_map:
                return [hash_map[target - value], index]
            hash_map[value] = index

    
    def twoSum5(self, nums: List[int], target: int) -> List[int]:
        # 2포인트터를 활용해서 풀어보자 정렬에 n log n, 탐색에 n 이므로 O은 가장 긴 값인 n log n 이다

        nums.sort()
        l, r = 0, len(nums) - 1  # 각각 시작할 인덱스 설정(인덱스이므로 전체 길이에서 -1)
        while l < r:
            if nums[l] + nums[r] > target: # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로(정렬상태이므로 최댓값을 낮춰본다)
                r -= 1
            elif nums[l] + nums[r] < target: # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로(정렬상태이므로 최솟값을 높여본다)
                l += 1

            if nums[l] + nums[r] == target:
                return True
        return False



  
solution=Solution()
answer = solution.twoSum4([11, 2, 15, 7], 9)
#output -> [1, 3]
print(answer)