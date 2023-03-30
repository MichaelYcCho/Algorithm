def solution(name, yearning, photo):
    # 그리움 점수를 이름과 매핑하는 딕셔너리를 생성
    yearning_dict = dict(zip(name, yearning))
    
    # 각 사진별 추억 점수를 저장할 리스트를 초기화
    memory_scores = []
    
    # 각 사진에 대해 추억 점수를 계산
    for p in photo:
        score = 0
        for person in p:
            # 인물의 그리움 점수가 있다면 누적
            if person in yearning_dict:
                score += yearning_dict[person]
        memory_scores.append(score)
    
    return memory_scores



name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
result = solution(name, yearning, photo)
print(result)