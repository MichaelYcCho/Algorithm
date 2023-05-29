def solution(phone_number):
    answer = []

    answer.append('*' * (len(phone_number)-4) + (phone_number[-4:]))
    return ''.join(answer)


phone_number = "01033334444"
print(solution(phone_number))




def hide_numbers(s):
    return "*"*(len(s)-4)+s[-4:]

print("결과 : " + hide_numbers('01033334444'));
