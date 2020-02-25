# DFS 깊이우선탐색 - 최장거리 탐색시 사용 

graph = {
    'A' : set(['B', 'C', 'E']),
    'B' : set(['A']),
    'C' : set(['A']),
    'D' : set(['E', 'F']),
    'E' : set(['A', 'D']),
    'F' : set(['D'])
}


def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        # .pop() 뒤에것을 꺼냄 
        current = stack.pop()

        count = 0
        print(f'{count}번째 current : {current}')
        if current not in visited:
            visited.append(current)
            print(set(graph[current]))
            stack += list(set(graph[current]) - set(visited))
            print(f'{count}번째 stack : {stack}')
            print(f'{count}번째 visited : {visited}')
            print(f'{count}번째 current : {current}')
            print(f'-------------------------')
    return visited


print(dfs(graph, 'E'))
