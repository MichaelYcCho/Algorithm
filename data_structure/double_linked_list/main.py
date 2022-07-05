from double_linked import DoubleLinkedList


def show_list(dlist):
    print('data size : {}'.format(dlist.size()))
    cur=dlist.head.next
    while cur is not dlist.tail:
        print(cur.data, end="  ")
        cur=cur.next
    print()

if __name__ == "__main__":
    dlist=DoubleLinkedList()
    print('*'*100)
    print('데이터 삽입 -add_first')
    # dlist.add_first(1)
    # dlist.add_first(2)
    # dlist.add_first(3)
    # dlist.add_first(5)

    print('데이터 삽입 -add_last')
    dlist.add_last(1)
    dlist.add_last(2)
    dlist.add_last(3)
    dlist.add_last(5)
    show_list(dlist)

    print('데이터 삽입 - insert_after')
    dlist.insert_after(4, dlist.search_forward(3))
    show_list(dlist)

    print('데이터 삽입 - insert_before')
    dlist.insert_before(4, dlist.search_forward(5))
    show_list(dlist)

    print('데이터 탐색')
    target=3
    #res=dlist.search_forward(target)
    res=dlist.search_backward(target)
    if res:
        print('데이터 {} 탐색 성공'.format(res.data))
    else:
        print('데이터 {} 탐색 실패'.format(target))
    res=None

    # print('데이터 삭제-delete_first')
    # dlist.delete_first()
    # dlist.delete_first()

    # print('데이터 삭제-delete_last')
    # dlist.delete_last()
    # dlist.delete_last()

    print('데이터 삭제-delete_node')
    dlist.delete_node(dlist.search_backward(5))

    show_list(dlist)

    print('*'*100)