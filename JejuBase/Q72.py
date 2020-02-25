# 너비우선탐색(BFS) - 최단경로를 구할때 사용 

graph = {
    'E' : set(['D', 'A']),
    'F' : set(['D']),
    'A' : set(['E', 'C', 'B']),
    'B' : set(['A']),
    'C' : set(['A']),
    'D' : set(['E', 'F'])
}



def dfs(graph, start):
    visited = []
    queue = [start]
    count = 0


    while queue:
        # stack과는 다르게 앞에서 꺼냄 
        n = queue.pop(0)

        print(f'{count}번째 current : {n}')
        if n not in visited:
            visited.append(n)
            print(set(graph[n]))
            queue += graph[n] - set(visited)
            print(f'{count}번째 queue : {queue}')
            print(f'{count}번째 visited : {visited}')
            print(f'{count}번째 current : {n}')
            print(f'-------------------------')
            count += 1
    return visited


print(dfs(graph, 'E'))
