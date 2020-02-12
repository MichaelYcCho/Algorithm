import re

input_user = input()
rule = re.compile('[a-c]+') #반복되는 a~ c를 찾아라

one = re.findall('b', input_user)
two = re.findall(rule, input_user)
three = re.findall('(\\w)(\\1*)', input_user)  #\\w 모든 문자열이 한번이상 반복되는 

print(one)
print(two)
print(three)

s = ' '
for i, j in three:
    s += str(len(j)+1) + i
print(s)

'''
정규표현식
[a-zA-Z] 알파뱃모두
\d 숫자
\w - 알파뱃숫자 모두 
\W - 문자와 숫자가 아닌 문자열들
^ 제외
*는 반복 + 는 반복
match, search, findall finditer
'''