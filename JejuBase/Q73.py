graph = {
    'A' : set(['B', 'C']),
    'B' : set(['A', 'D', 'E']),
    'C' : set(['A', 'F']),
    'D' : set(['B']),
    'E' : set(['B', 'F']),
    'F' : set(['C', 'E'])
}


start, end = [i for i in input().split(' ')]

queue = [start]
visited = [start]


def solution():
    count = -1

    #queue는 비기전까지 순회함 단 start와 end 노드가 일치한다면 멈춤
    while len(queue) != 0:
        count += 1
        size = len(queue)
        print(f'count는 {count}')
        #queue에 담긴 노드들은 모두 visited에 추가되어야 하기때문에 size만큼 반복
        for i in range(size):
            node = queue.pop(0)
            print(f'    node는 {node}')
            if node == end:
                return count

            #만약 시작이 A라면 grapth[node]는 A의 값인 B, C가되는것 이렇게 노드를 잇는 역할을 함 
            for next_node in graph[node]:
                print(f'        graph[node]는 {graph[node]}')
                print(f'        next_node는 {next_node}')
                if next_node not in visited:
                    queue.append(next_node)
                    visited.append(next_node)
                    print(f'            visitied는 {visited}')
                    print(f'            queue는 {queue}')

    return count


print(solution())