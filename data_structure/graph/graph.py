class Graph:
    def __init__(self, vertex_num=None) -> None:
        # 인접 리스트
        self.adj_list = []
        self.vtx_num = 0
        # 정점이 있으면 True 없으면 False
        self.vtx_arr = []

        #정점 개수를 매개변수로 넘기면 초기화
        if vertex_num:
            self.vtx_num(vertex_num)
            self.vtx_arr = [True for _ in range(self.vtx_arr)]
            # 배열 요소로 연결 리스트 대신 동적배열을 사용
            self.adj_list = [[] for _ in range(self.vtx_num)]

    def is_empty(self):
        if self.vtx_num == 0:
            return True
        return False
    
    def add_vertex(self):
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