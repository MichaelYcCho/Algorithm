import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
q_list = list(map(int, input().split()))
#print(q_list)

lt = 0
rt = 1
tot = q_list[0]
cnt = 0


while(True):
    if tot < m:
        if rt < n:
            tot += q_list[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= q_list[lt]
        lt += 1
    else:
        tot -= q_list[lt]
        lt += 1

print(cnt)
    



'''
for i in range(len(q_list)):
    if q_list[i] == m:
        cnt += 1
        break
    for j in range(i+1, len(q_list)):
        print('합', q_list[i], q_list[j], '합') 
        surplus = 0
        sum_e =  q_list[i] + q_list[j]
        #print(q_list[i], '흠')


        if sum_e < m:
            surplus += 1
            sum_e += q_list[j + surplus]

        if sum_e == m:
            print('헷')
            cnt += 1
            break

print(cnt)
'''