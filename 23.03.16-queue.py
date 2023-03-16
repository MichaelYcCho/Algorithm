from collections import deque
from queue import Queue

# deque를 이용한 큐 구현
queue1 = deque([1, 2, 3])
queue1.append(4)
queue1.append(5)
print(queue1.popleft())
print(queue1.popleft())
print("==================")
print()

# queue를 이용한 큐 구현
queue2 = Queue()
queue2.put(1)  # enqueue의 append와 같은 역할
queue2.put(2)
queue2.put(3)
print(queue2.get())  # dequeue의 popleft와 같은 역할
print(queue2.get())
print(queue2.get())


# List를 이용한 큐 구현
queue3 = [1, 2, 3]
queue3.append(4)
queue3.append(5)
print(queue3.pop(0))
print(queue3.pop(0))
