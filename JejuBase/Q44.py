#각 자리수 합
n = input()
result = 0
print(n)

for i in n:
    print(f"{i}번쨰 글자는 {[i]}입니다.")
    result += int(i)

print(result)