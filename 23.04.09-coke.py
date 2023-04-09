# 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있을 때, 빈 병 n개를 가져다주면 몇 병을 받을 수 있는지 계산하는 문제

def solution(a, b, n):
    answer = 0
    # 단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다.
    # 빈 병의 개수가 콜라를 받기 위해서 필요한 개수보다 크면 반복한다
    while (n >= a):
        remain_bottle = n % a
        n = (n//a) * b # 마트에서 받은 콜라의 수
        answer += n # 받은 걸 answer에 +
        n += remain_bottle # 남아있는 병을 더해줘서 다음에 마트갈 때 이용
    return answer