# Q8
'''
d = {'height':180, 'weight':78, 'weight':84, 'temparture':36, 'eyesight': 1}
print(d['weight'])
print(type(d['eyesight']))
'''


# Q9
'''
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'


print(year, month, day, sep="/", end=" ")
print(hour, minute, second, sep=":", end="끝")
'''


# Q10
'''
user_input = 5
print("Hello your input is " + f"{user_input}")

n = 5
for i in range(1, 6):
    print(' '*(n-i) + '*'*(2*i-1))
'''


# Q11 1부터 100까지 합
'''
s = 0

for i in range(1, 101):  
    s +=  i
    if(i == 100):
        print(s)
'''

# Q12 클래스로 능력치 및 배기출력

'''
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    

    def slash(self):
        print("베기")


x = Knight(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.slash()
'''

'''
# Q13 n번째 행성은 ~ 입니다.
user_input = 1
l = ['수성', '금', '지', '화', '목', '토', '천', '해', '명']
print(l[user_input-1])


'''
'''
# Q 15 
user_input = input()
print(f"안녕하세요 저는 {user_input} 입니다.")
print("안녕하세요 저는" + user_input + "입니다.")

'''
'''
#Q16 문자를 입력하면 거꾸로 출력
user_input = input()
print(user_input[::-1])

'''
'''
# Q18 과목 평균
user_input = input()
l = user_input.split(' ')
print(l)
changel = []

for i in l:
    changel.append(int(i))

print(sum(changel)//3)


l = ['20']
x = int(l[0])
print(x)
'''

