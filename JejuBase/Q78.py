user_input = input().split(' ')
n, k = user_input

def sol(n, k):
    # i = 인덱스
    i = 0

    # 전체 접시를 순회하는 리스트 
    q = [i for i in range(1, n+1)]

    # 2개의 접시 이상이 남는 동안(즉 접시가 2개되면 탈출)
    while len(q) > 2:
        print(f'i : {i}')
        print(f'q : {q}')
        # 인덱스를 초과하는 경우 다시 처음으로 돌려보내서 순회시켜야함
        if i > len(q)-1: 
            i -= len(q)  
        q.pop(i)
        print('-------------------')
        i += k -1


    return q

print(sol(int(n), int(k)))
