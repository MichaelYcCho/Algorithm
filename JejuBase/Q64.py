# 무게 맞춰서 운반하기

value = int(input())
result = 0

while True:
    if value % 7 == 0:
        result += value//7
        print(result)
        break
    value -= 3 # 7로 나눠지지 않는경우 3kg선택지밖에 없기때문에 3을 제함 
    result += 1 # 즉 이문구는 3kg을 한번 옮기고 result 에 1을 증가시킨것
    if value < 0:
        print(-1)
        break