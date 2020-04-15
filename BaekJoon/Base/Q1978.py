n = int(input())
l = list(map(int, input().split()))
count = 0

for i in l:
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
        #if i % j != 0:
            count += 1

print(count)   


# for ~ else문



'''
n = int(input())
l = list(map(int, input().split()))
answer = 0

for i in l:
    count = 0
    if i != 1:
        for j in range(2, i+1):
            if i % j == 0:
                count += 1
        if (count == 1) :
            answer += 1


print(answer)




# 중복된 수를 배제하기 위해 일단 다 count로 적립하고 그수가 1이라는 것은
# 나눠지는 수가 자기자신뿐이라는 뜻이니 이 수를 다시 카운팅함

'''