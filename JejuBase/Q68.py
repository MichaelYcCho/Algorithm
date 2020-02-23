def 분으로변환(문자열):
    return int(문자열.split(':')[0]) * 60 + int(문자열.split(':')[1])

def 시간으로변환(분):
    return '{0:02d}:{1:02d}'.format(분//60, 분%60)


# '{0:02d} {0번째 인자를 0으로 채우면서 2자리 자연수02d 로}  :{}'.format(분//60, 분%60)  

#print(분으로변환('12:30'))
#print(시간으로변환(분으로변환('12:30')))
#print('{0:^50}'.format(999))
#print('999'.zfill(10))




def sol(시간리스트, 현재시간):
    answer = []
    for 시간 in 시간리스트:
        if 분으로변환(시간) - 분으로변환(현재시간) < 0:
            answer.append('지나갔습니다.')
        else:
            answer.append(시간으로변환(분으로변환(시간) - 분으로변환(현재시간)))


    return answer

print(sol(["12:30", "12:40", "13:20", "14:13"], "12:40"))