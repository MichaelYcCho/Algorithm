
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return l-i
    return 0



citations = [3, 0, 6, 1, 5]

print(solution(citations))

"""
만약 
citations = [3, 0, 6, 1, 5]
라면
발표된 논문은 총 5개
그중 인용된 논문의 경우는
6번, 총 1
5번 이상, 총 2 [5, 6]
3번 이상, 총 3 [3, 5, 6]
1번 이상, 총 4 [1, 3, 5, 6]
0번 이상 ~ 총 5

이때 만약 h가 1이라면 1편 이상 언급된 논문은 4이므로 h의 변수가 1 !=4 로 틀리게 된다.
따라서 3번이상 3이 h의 최대값이 되는것이다. 


Case2
citations = [10,9,8,0]

답 : 3



8이 h라고 처음에 ㄴ생각했으나 답은 3이다. 



어떤 과학자가 발표한 논문 4편 중, 3번 이상 인용된 논문이 3편 이상(10, 9, 8)이고 나머지 논문이 3번 이하(1) 인용되었기 때문이다.



"""