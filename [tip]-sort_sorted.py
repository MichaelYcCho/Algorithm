"""
리스트.sort() 는 본체의 리스트를 정렬해서 변환,
sorted(리스트) 는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환
"""
a = [1, 3, 2, 4, 5]

# 본체의 리스트를 정렬해서 변환
a.sort() # None
print(a) # [1, 2, 3, 4, 5]


# 정렬한 새로운 리스트로 반환
sorted(a) # [1, 2, 3, 4, 5]
print(a) # [1, 3, 2, 4, 5]

# 글자 수를 기반으로 sorting하는법
b = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(b, key=len) ) # ['d', 'bb', 'ccc', 'aaaa']


# 첫 문자열 + 마지막 문자열 순으로 정렬

d = ['cde', 'cfc', 'abc']
def fn(s):
    return s[0] + s[-1]

print(sorted(d, key=fn)) # ['abc', 'cfc', 'cde']
print(sorted(d, key=lambda x: x[0] + x[-1])) # ['abc', 'cfc', 'cde']
