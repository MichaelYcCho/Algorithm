import sys
#sys.stdin = open('input.txt', 'r')

def each_sum_num(x):
    each_num = str(x)
    sum_num = 0
    for i in each_num:
        sum_num += int(i)
    return sum_num


n = int(input())
num_list = list(map(int, input().split()))

max_num = 0
result = 0
for x in num_list:
    if each_sum_num(x) > max_num:
        max_num = each_sum_num(x)
        result = x

print(x)

'''
def digit_sum(x):
    sum = 0
    #str_n = list(str(x))

    for i in str(x):
        sum += int(i)
      
    return sum 


    또는

    sum = 0
    while x > 0:
        sum +=x%10
        x=x//10




n =  int(input())

a = list(map(int, input().split()))

max = 0
for x in a:
    tot = digit_sum(x)

    if tot > max:
        max = tot
        res = x

print(x)
'''
