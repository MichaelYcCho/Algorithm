class CQueue:
    MAXSIZE = 10

    def __init__(self):
        self.container = [None for _ in range(CQueue.MAXSIZE)]
        self.front = 0
        self.rear = 0

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

    # front나 rear를 뒤로이동했을때 동정 배열을 벗어나면 배열의 맨 처음으로 이동
    def __step_forward(self, x):
        x +=1
        if x >= CQueue.MAXSIZE:
            x = 0
        return x

    def is_full(self):
        next = self.__step_forward(self.rear)
        if next == self.front:
            return True
        return False
    
    def enqueue(self, data):
        if self.is_full():
            raise Exception("Queue is full")
        self.container[self.rear] = data # 해당 rear에 데이터 삽입
        self.rear = self.__step_forward(self.rear) # 마지막으로 삽입한 데이터의 다음을 가리킨다. 



    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        ret = self.container[self.front]
        self.front = self.__step_forward(self.front)
        return ret

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        return self.container[self.front]