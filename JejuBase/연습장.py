from itertools import permutations, combinations


test = [1, 2, 3, 4, 5, 6]

# 조합 : 위치가 달라도 내용물이 같다면 같은 개체로인식
print(list(combinations(test, 2)))

# 순열: 위치가 다르다면 다른 개체로 인식
print(list(permutations(test, 2)))
