def sol(n):
    n = list(str(n))
    print(n)
    answer = 0  # 응답할 값
    count = 1
    d = {3:1, 6:2, 9:3}

    while n:
        print('-1 ->', n[-1])
        answer += d[int(n.pop())] * count
        count *= 3   # 3의 제곱 역할 

    return answer

print(sol(66))


'''
숫자에 3, 6, 9의 숫자만 들어갈때 횟수 카운팅

숫자 // 횟수  //합
 
3 = 1   //1
6 = 1   //2
9 = 1   //3
33 = 1*3 + 1  //4
36 = 1*3 + 2  //5
39 = 1*3 + 3  //6

63 = 2*3 +1 //7
93 = 3*3+1  //10
...

333 = 1*9 + 1*3 + 1





'''