

"""
    .index(x) 리스트에서 x의 인덱스 retrun
    .index(x, start) 리스트[start:]에서 x의 인덱스 return
    .index(x, start, stop) 리스트[start:stop]에서 x의 인덱스 return
        ( -> start부터 stop-1까지의 원소들만 포함)
"""

a = [11, 10, 12, 13, 20, 31, 11, 10, 10, 11]

# list a에서 10의 위치 찾기, 10이 여러개 있으면 가장 앞에 있는 10의 위치를 반환한다
print(a.index(10)) # 1

# list a에서 2 ~ 9 번쨰 위치에서 10의 위치 찾기 
print(a.index(10, 2, 9)) # 7


b = '123451'

# 문자열 b에서 '1'의 위치 찾기, 1이 여러개 있으면 가장 앞에 있는 1의 위치를 반환한다
print(b.index('1')) # 0

# 문자열 b에서 1 ~ 6 번쨰 위치에서 '1'의 위치 찾기
print(b.index('1', 1, 6)) # 5