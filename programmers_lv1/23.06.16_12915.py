def solution(strings, n):
    strings.sort() 
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n))  # 결과: ['car', 'bed', 'sun']



# sorted까지 한번에 
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])
strings = ["sun", "bed", "car"] 
print(strange_sort(strings, 1))