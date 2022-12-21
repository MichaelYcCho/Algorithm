s = ['2 A', '1 B', '4 C', '1 A']

# 가장 앞에있는 문자열을 기준으로 정렬
print(sorted(s)) # ['1 A', '1 B', '2 A', '4 C']


# 1. 문자열 정렬 후 2. 숫자 정렬
s.sort(key=lambda x: (x.split()[1], x.split()[0]))
print(s) # ['1 A', '2 A', '1 B', '4 C'] 