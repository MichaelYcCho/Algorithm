def solution(todo_list, finished):
    answer = []
    for idx, val in enumerate(finished):
        if val == False:
            answer.append(todo_list[idx])
    return answer


def solution(todo_list, finished):
    answer = []
    for todo, fin in zip(todo_list, finished):
        if fin == False:
            answer.append(todo)
    return answer
