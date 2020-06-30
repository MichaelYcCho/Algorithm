import sys
sys.stdin = open('input.txt', 'r')


def digit_sum(x):
    sum = 0
    #str_n = list(str(x))

    for i in str(x):
        sum += int(i)
      
    return sum 


    '''
    또는

    sum = 0
    while x > 0:
        sum +=x%10
        x=x//10

    '''



n =  int(input())

a = list(map(int, input().split()))

max = 0
for x in a:
    tot = digit_sum(x)

    if tot > max:
        max = tot
        res = x

print(x)
