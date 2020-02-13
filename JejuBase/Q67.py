# 악수 
# time = 내가 악수한 횟수 
# total = 전체악수횟수


def sol(n):
    people = 0
    total = 0
    while(True):
        temp = total # 여기서 임시변수에 넣어두지 않으면 total이 한번 더 더해진 채로 계산됨
        total = (people*(people-1))//2
        if n < total:  #내가 악수한 사람들보다 많아졌다는 뜻
            break
        print(temp, total)
        people += 1
    times = n - temp
    return [times, people]

i = int(input())
print(sol(i))