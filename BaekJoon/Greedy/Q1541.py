example = input().split('-')
print(f'1단계 {example}')

result = 0

for i in example[0].split('+'):
    print(example[0])
    result += int(i)


for i in example[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
