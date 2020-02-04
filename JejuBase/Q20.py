user_input = input()
l = user_input.split(' ')
changel = []

for i in l:
    changel.append(int(i))
print(changel[0]//changel[1], end=" ")
print(changel[0]%changel[1])


# 방법2
user_input = input()
l = [ int(i) for i in user_input.split(' ')]
print(l[0]//l[1], l[0]%l[1])