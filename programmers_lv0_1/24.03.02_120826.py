def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    return answer


def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer