graph = {
    100: set([67, 66]),
    67: set([100, 82, 63]),
    66: set([100, 73, 69]),
    82: set([67, 61, 79]),
    63: set([67]),
    73: set([66]),
    69: set([66, 65, 81]),
    61: set([82]),
    79: set([82, 87, 77]),
    65: set([69, 84, 99]),
    81: set([69]),
    87: set([79, 31, 78]),
    77: set([79]),
    84: set([65]),
    99: set([65]),
    31: set([87]),
    78: set([87]),
}
# 최소값 순회 ex) min(graph[100])


# 깊이우선탐색은 stack, 너비우선 탐색은 Queue
def 깊이우선탐색(graph, start):
    방문 = []  # 방문한 노드를 기록할 리스트
    stack = [start]  # 탐색할 노드를 담는 스택, 시작 노드로 초기화

    while stack:  # 스택이 비어있지 않는 동안 반복
        n = stack.pop()  # 스택에서 노드를 꺼냄, ex) 100
        if n not in 방문:  # 꺼낸 노드를 방문하지 않았다면
            # print("n이뭔데", n)
            방문.append(n)  # 방문 리스트에 추가
            차집합 = graph[n] - set(방문)  # ex) {66, 67} - {100} = {66, 67}
            if len(차집합) == 0:
                방문 += stack
                break
            # 작은값 우선 순회(min)
            stack.append(min(차집합))  # 스택에 추가 [66, 67]
            print(f"visited: {방문}")
            print(f"stack : {stack}, \n")
    return 방문  # 모든 노드를 방문한 후, 방문 순서를 반환


code = 깊이우선탐색(graph, 100)
print(code)
resolve = "".join([chr(i) for i in code])
print(resolve)
