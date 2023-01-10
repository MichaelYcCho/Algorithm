"""
해시 테이블 
ken in  {} 가 핵심

정렬되어있지 않은 정수형 배열 nums에서 nums 원소를 가지고 만들 수 있는 가장 긴 연속된 수의 갯수

"""

nums = [100, 4, 200, 1, 3, 2]
# output = 4(가장 긴 연속된 수의 갯수[1, 2, 3, 4])

"""
Way1. 정렬 후 for을 통해 연속된수
Way2. HashTable을 사용하여 for문을 통해 연속된 수 파악 (해당 for문은 연속)
"""

def longestConsecutive1(nums):
    longest = 0
    num_dict = {}
    
    # 메모리에 하나하나 저장, 키값으로 관리하여 중복을 막는 역할도 할 수 있다.
    for num in nums:
        num_dict[num] = True
    
    for num in num_dict:
        # 연속된 수를 찾기 위해 앞의 수가 없는 경우를 찾아야한다.
        """
        첫번째 케이스를 예로들면 num : 6, 
                        (num - 1) : 5 
        즉 5가 있으므로 굳이 6부터 시작할 이유가 없어진다. 따라서 최초의 수가 나올때까지 진행하지 않는다.
        """
        if num - 1 not in num_dict:  
            cnt = 1  # 위의 사례면 100부터 시작하게됨
            target = num + 1  
            """
            while에 쓰인 in은 조건문이다. 즉 target(101)이 num_dict에 있으면 True,  
            하지만 101이 없으므로 다음 인덱스의 for문으로 넘어간다.
            """
            while target in num_dict: 
                cnt += 1
                target += 1
            longest = max(longest, cnt)
    return longest

answer1= longestConsecutive1([6, 7, 100, 5, 4, 4])
print(answer1)