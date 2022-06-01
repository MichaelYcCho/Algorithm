# 연결 리스트

"""
data는 실제 저장하려는 data
link는 다음 노드를 가리킨다. 
이렇게 참조로 데이터와 데이터를 연결(link)해두는 리스트를 연결 리스트 라고한다. 

단순연결리스트는 담은 노드를 가리키는 참조하나
이중연결리스트는 앞 노드를 가리키는 참조와 뒤 노드를 가리키는 참조를 모두 가지고있다. 
"""

class Node:
    def __init__(self, data=None) -> None:
        self.__data = data
        self.__prev = None  # 이전 노드참조
        self.__next = None  # 다음 노드 참조
    
    # 소멸자: 객체가 사라지기전 반드시 호출
    # 삭제 연산 때 삭제된느 것을 확인
    def __del__(self):
        print(f"data of {self.data} is deleted")
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
        
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, p):
        self.__prev = p
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, n):
        self.__next = n
        
        
    