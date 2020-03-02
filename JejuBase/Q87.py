name = '손오공 야모차 메지터 비콜로'.split(' ')
point = list(map(int, '70 10 55 40'.split(' ')))


def rank_num(x):
    return x[1]

def sol(name, point):
    d = {}
    z = [[i, j] for i, j in zip(name, point)]
    z = sorted(z, key=rank_num, reverse=True)
    # return z

    for i in range(len(z)):
        d[z[i][0]] = i + 1
    return d

print(sol(name, point))



'''
key= 사용서

def hojun(x):
    return len(x)

test = 'AA CCCC BB D'.split(' ')
sorted(test, key=hojun)



'''