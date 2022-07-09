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