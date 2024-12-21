"""
	1.	str(age)
	•	숫자 age를 문자열로 변환합니다. 예를 들어, age = 23이면 "23"이 됩니다.
	2.	for i in str(age):
	•	문자열 "23"의 각 문자 "2"와 "3"를 순회합니다.
	3.	int(i) + 97
	•	각 문자를 정수로 변환합니다.
예: "2" → 2, "3" → 3
	•	97은 알파벳 'a'의 ASCII 코드입니다.
따라서 int(i) + 97은 숫자를 알파벳에 대응시킵니다.
예: 2 → 'c' (ASCII: 99), 3 → 'd' (ASCII: 100)
	4.	chr()
	•	정수를 문자로 변환합니다.
예: 99 → 'c', 100 → 'd'.
	5.	answer += ...
	•	변환된 알파벳을 answer 문자열에 추가합니다.
예: 처음에는 빈 문자열 "", "c"를 추가하면 "c", 이후 "d"를 추가하면 "cd".
	6.	return answer
	•	변환이 완료된 문자열을 반환합니다.
"""


def solution(age):
    answer = ""
    for i in str(age):
        answer += chr(int(i) + 97)
    return answer


def solution(age):
    answer = ""
    reg = {
        "0": "a",
        "1": "b",
        "2": "c",
        "3": "d",
        "4": "e",
        "5": "f",
        "6": "g",
        "7": "h",
        "8": "i",
        "9": "j",
    }
    for i in str(age):
        answer += reg[i]
    print(answer)
    return answer
