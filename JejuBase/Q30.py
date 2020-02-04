data = input()
word = input()

print(data.find(word))

'''
찾는문자열이 없을 경우
find()는 -1을 반환하지만 
index()는 에러로 귀결됨 따라서 find를 쓰는것이 더 용이함 
'''