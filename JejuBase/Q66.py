def solution(allBlock, rule):
    answer =[]
    for i in allBlock:
        answer.append(blockCheck(i, rule))
    return answer 

def blockCheck(partBlock, rule):
    temp = rule.index(rule[0])
    for j in partBlock:
        print(j)
        if j in rule: #문자가 규칙에 있다면 
            # 만약 c가 2, D가 3일때 ABDC였다면  3>2가 되므로 이는 순서에 어긋났다는 것을 예측할 수 있음 
            if temp > rule.index(j): 
                return '불가능'
            temp = rule.index(j)
    return '가능'


allBlock = input().split(' ')
#['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG']
rule = input()
#'ABD'
    
print(solution(allBlock, rule)) 

'''
def solution(전체블록, 규칙):
    answer =[]
    for 부분블록 in 전체블록:
        answer.append(블록순서체크(부분블록, 규칙))
    return answer 

def 블록순서체크(부분블록, 규칙):
    임시변수 = 규칙.index(규칙[0])
    for 문자 in 부분블록:
        if 문자 in 규칙:
            # 만약 c가 2, D가 3일때 ABDC였다면  3>2가 되므로 이는 순서에 어긋났다는 것을 예측할 수 있음 
            if 임시변수 > 규칙.index(문자): 
                return '불가능'
            임시변수 = 규칙.index(문자)
    return '가능'


전체블록 = input().split(' ')
#['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG']
규칙 = input()
#'ABD'
    
print(solution(전체블록, 규칙)) 
'''