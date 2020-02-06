# Q34. 입력받은 input값이 정렬되어있지 않다면 No 출력 

user_input = input()
l = list(user_input.split())
l = [int(i) for i in l]
#print(sorted(l))

if l != sorted(l):
    print("No")
else:
    print("Yes")


'''
sort는 리스트를 직접적으로 다루는 리스트 내장함수
sorted는 return된 값을 정렬해서 출력해줌
'''