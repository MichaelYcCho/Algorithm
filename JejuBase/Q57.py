# 1 개수세기

def count(n):
    #방법 1
    '''
    s = str(list(range(n+1)))
    count = 0
    for i in s:
        if i == '1':
            count += 1
    return count
'''
    #방법2
    count = str(list(range(n+1))).count('1')

    return count


print(count(1000))