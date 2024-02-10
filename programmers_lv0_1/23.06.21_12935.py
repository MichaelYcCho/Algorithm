def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        
        return arr
    else:
        return [-1]
    
    
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        arr.remove(min(arr))
        arr.insert(0,-1)
        return arr
        
print(solution([4,3,2,1]))
print(solution([10]))