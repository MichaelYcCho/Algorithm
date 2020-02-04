key = input().split(' ')
value = map(int, input().split(' '))
#print(key, list(value))

result = dict(zip(key, value))
#for key, value in zip(key, value):
#    print(key, value)
print(result)
