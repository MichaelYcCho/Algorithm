def solution(numbers, target):
    answer_tree=[0]
    for number in numbers:
        node_list=[]
        for tree_number in answer_tree:
            node_list.append(tree_number+number)
            node_list.append(tree_number-number)
        answer_tree=node_list
    answer = answer_tree.count(target)
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3


print(solution(numbers, target))