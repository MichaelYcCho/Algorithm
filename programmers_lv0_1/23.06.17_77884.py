def solution(left, right):
    answer = 0
    for i in range(left, right+1):	
        now_count = 0;			
        for j in range(1, i+1):		
            if i % j == 0:		
                now_count +=1;		
        
        if now_count % 2 == 0:		
            answer += i			
        else:
            answer -= i			
            
    return answer			





'''
제곱수를 제외한 모든 정수들의 약수의 개수는 무조건 짝수 개수이며 제곱수만 홀수 개수임을 알았다면 아래처럼 풀 수 있다. 수학적 사고.
2를 제곱근으로 가지는 4는 1,2,4 이렇게 3개, 
5를 제곱근으로 가지는 25는 1,5,25 로 3개. 
반면 10의 제곱근은 3.1622776601683795 으로 정수가 아닌데 10의 약수는 1,2,5,10 이렇게 4개로 짝수
'''
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer