start = 1
end = 7
queue = [1]
visited = [1]

# 1차순회

def solution(1, []]):
    if 1 == end:
        return len([])
    # 마지막에들어온값이 visited안에있다면 다시 순회할 필요가 없으므로 종료 
    if 1 in visited:
        return len([])

    visited.append([1])
    length = 0

    for next_node in graph[1]:
        n.append(next_node)
        # 둘을 비교해서 둘중 최대값을 반환함
        length = max(length, solution(n, visited))
        queue.pop(-1)
    return length


print(solution(queue, visited))





def solution(1, []]):
    if 1 == end:
        return len([])
    # 마지막에들어온값이 visited안에있다면 다시 순회할 필요가 없으므로 종료 
    if 1 in visited:
        return len([])

    visited.append([1])
    length = 0

    # 1: 의 값인 2, 3, 4가 하나씩 순회함 
    for next_node in graph[1]: # 2가 순회하면서 없으므로 queue = [1, 2] 가 됨
        n.append(next_node)  
        # 둘을 비교해서 둘중 최대값을 반환함
        length = max(0, solution(n, visited))
        queue.pop(-1)
    return length


print(solution(queue, visited))




# 2차 순회

start = 1
end = 7
queue = [1, 2]
visited = [1]



def solution([1, 2], [1]):
    if 2 == end:
        return len([1])
    # 마지막에들어온값이 visited안에있다면 다시 순회할 필요가 없으므로 종료 
    if 2 in visited:
        return len([1])

    visited.append(2)
    length = 0

    # 1: 의 값인 2, 3, 4가 하나씩 순회함 
    for next_node in graph[2]: 
        [1, 2].append(next_node)  
        # 둘을 비교해서 둘중 최대값을 반환함
        length = max(0, solution([1, 2], visited))
        queue.pop(-1)
    return length


print(solution(queue, visited))
