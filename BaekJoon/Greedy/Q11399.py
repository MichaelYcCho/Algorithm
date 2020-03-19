count = int(input())
val = list(map(int, input().split()))
val = sorted(val)

    

def sol():
    answer = 0

    for i in range(count):
        print(f'--------------i는 {i}--------------')
        for j in range(i+1):
            print(f'j는 {val[j]}')
            answer += val[j]
            print(answer)
    
    return answer


print(sol())

