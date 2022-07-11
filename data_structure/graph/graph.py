class Graph:
    def __init__(self, vertex_num=None) -> None:
        # 인접 리스트
        self.adj_list = []
        self.vtx_num = 0
        # 정점이 있으면 True 없으면 False
        self.vtx_arr = []

        #정점 개수를 매개변수로 넘기면 초기화
        if vertex_num:
            self.vtx_num=vertex_num
            self.vtx_arr=[True for _ in range(self.vtx_num)]
            # 배열 요소로 연결 리스트 대신 동적배열을 사용
            self.adj_list = [[] for _ in range(self.vtx_num)]

    def is_empty(self):
        if self.vtx_num == 0:
            return True
        return False
    
    def add_vertex(self):
        """ 추가된 정점의 정점 인덱스를 반환"""
        for i in range(len(self.vtx_arr)):
            # 중간에 상제된 정점이 있으면 이를 재사용
            # vtx_arr == False 은 삭제된 정점
            if self.vtx_arr[i] == False:
                self.vtx_num += 1
                self.vtx_arr[i] = True
                return i

        # 삭제된 정점이 없으면 새로운 정점을 추가
        self.adj_list.append([])
        self.vtx_num += 1
        self.vtx_arr.append(True)
        return self.vtx_num - 1

    def delete_vertex(self, v):
        if v >= self.vtx_num:
            raise Exception(f"There is no vertex of {v}")
        # 정점 v가 있을때
        if self.vtx_arr[v]:
            # 정점 v의 인접 정점 집합을 초기화함
            self.adj_list[v]=[]
            self.vtx_num-=1
            self.vtx_arr[v]=False
            #  나머지 정점 중 v와 인접합 정점이 있다면
            # 그 정점의 리스트에서 v를 제거
            for adj in self.adj_list:
                for vertex in adj:
                    if vertex==v:
                        adj.remove(vertex)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    
    def delete_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def adj(self, v):
        return self.adj_list[v]

# 그래프를 편하게 보기 위한 편의 함수
def show_graph(g):
    print(f"num of vertices : {g.vtx_num}")
    print("vertices : {", end="")
    for i in range(len(g.vtx_arr)):
        if g.vtx_arr[i]:
            print(f"{i}, ", end="")
    print("}")
    for i in range(len(g.vtx_arr)):
        if g.vtx_arr[i]:
            print(f"[{i}] : {{", end="")
            for j in g.adj_list[i]:
                print(f"{j}, ", end=" ")
            print("}")

if __name__=="__main__":
    g=Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    show_graph(g)
    print()

    added=g.add_vertex()
    g.add_edge(added, 1)
    g.add_edge(added, 2)
    show_graph(g)
    print()

    g.delete_vertex(2)
    show_graph(g)
    print()

    added=g.add_vertex()
    print(added)
    g.add_edge(added, 1)
    g.add_edge(added, 4)
    show_graph(g)
    print()