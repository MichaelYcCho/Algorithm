def solution(n):
    answer = ''

    while n > 0:			
        n, re = divmod(n, 3)	# n을 3으로 나눈 몫과 나머지
        answer += str(re)
    return int(answer, 3)



# divmod() : 몫과 나머지를 리턴하는 내장함수. 
# int(answer, 3)에서 3은 answer가 3진법으로 표현되어 있다는 것을 의미하며, 이를 10진법으로 변환해야 함을 나타냅니다.