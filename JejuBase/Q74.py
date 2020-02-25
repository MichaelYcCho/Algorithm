graph = {
    1: [2, 3, 4],
    2: [1, 3, 4, 5, 6],
    3: [1, 2, 7],
    4: [1, 2, 5, 6],
    5: [2, 5, 6, 7],
    6: [2, 4, 5, 7],
    7: [3, 5, 6]


}



start, end = [int(i) for i in input().split()]
queue = [start]
visited = []
# print(start, end)

def solution(n, visited):
    if n[-1] == end:
        return len(visited)
    # 마지막에들어온값이 visited안에있다면 다시 순회할 필요가 없으므로 종료 
    if n[-1] in visited:
        return len(visited)

    visited.append(n[-1])
    length = 0

    for next_node in graph[n[-1]]:
        n.append(next_node)
        # 둘을 비교해서 둘중 최대값을 반환함
        length = max(length, solution(n, visited))
        queue.pop(-1)
    return length


print(solution(queue, visited))