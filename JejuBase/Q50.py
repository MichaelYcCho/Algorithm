# 버블정렬

def bubble(n, data):
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                '''
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp
                '''
    for i in range(n):
        print(data[i], end= " ")

n = int(input()) # 몇개 값을 입력할것인지 
data = list(map(int, input().split()))

bubble(n, data)