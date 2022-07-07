from circle_queue import CQueue

if __name__ =="__main__":
    cq=CQueue()

    for i in range(8):
        cq.enqueue(i)

    for i in range(5):
        print(cq.dequeue(), end="  ")

    for i in range(8, 14):
        cq.enqueue(i)

    while not cq.is_empty():
        print(cq.dequeue(), end="  ") 

    print()
    for i in range(10):
        print(cq.container[i], end="  ")