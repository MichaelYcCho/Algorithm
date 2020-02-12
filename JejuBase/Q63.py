user_input = input().split()


print(user_input)
result = ''

for s in user_input:
    result += s[0]

print(result)