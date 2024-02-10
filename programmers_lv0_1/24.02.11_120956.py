def solution(babbling):
    result = 0
    babbling_list = ['aya', 'ye', 'woo', 'ma']

    for i in babbling:
        cnt = 0
        word = ''
        for j in i:
            word += j 
            if word in babbling_list:
                cnt += 1
                word = ''
        
        if len(word) == 0 and cnt > 0:
            result += 1
    return result


print(solution(["aya", "yee", "u", "maa", "wyeoo"])) # 1
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])) # 3