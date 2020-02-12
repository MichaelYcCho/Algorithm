# 방법1
s = 'hi'
print("{0:<50}".format(s) + '!!')
print("{0:>50}".format(s) + '!!')
print("{0:0.4f}".format(3.141598727))
print("{0:-^50}".format(s))


# 방법2

s = ('='*((50-len(s))//2)) + s + ('='*((50-(50-len(s))//2)-len(s)))
print(s)