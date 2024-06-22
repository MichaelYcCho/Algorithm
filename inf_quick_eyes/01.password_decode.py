text = [
    "   + -- + - + -   ",
    "   + --- + - +   ",
    "   + -- + - + -   ",
    "   + - + - + - +   ",
]

# ord(); 문자 -> 숫자
# chr()ㅣ 숫자 -> 문자

result_list = []
# 1. 공백문자 제거
for i in text:
    convert_int = int(i.strip().replace(" ", "").replace("+", "1").replace("-", "0"), 2)
    # 2진법으로 변형
    result_list.append(chr(convert_int))


print("".join(result_list))
