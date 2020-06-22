
def solution(p, s):
    p = list(map(int, p))
    s = list(map(int, s))
    answer_tree = []


    for i in range(len(p)):
        node_list = []
        count_A = 0
        count_B = 0
        while True:
            p[i] += 1
            count_A +=1
            if p[i] > 9:
               p[i] = 0
            elif p[i] < 0:
                p[i] = 9
            if p[i] == s[i]:
                count = min(count())

            




p = "82195"	
s = "64723"	



print(solution(p, s))