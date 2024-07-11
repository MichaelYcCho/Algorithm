from collections import deque, defaultdict


def count_hits(requests, cache_size):
    cache = deque()
    cache_set = set()
    hits = 0

    for request in requests:
        if request in cache_set:
            hits += 1
            cache.remove(request)
            cache.append(request)
        else:
            if len(cache) == cache_size:
                removed = cache.popleft()
                cache_set.remove(removed)
            cache.append(request)
            cache_set.add(request)
    return hits


def getMinimumSize(requests, k):
    n = len(requests)
    left, right = 1, n
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if count_hits(requests, mid) >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


# 예제 테스트
print(getMinimumSize(["item3", "item2", "item1", "item2", "item3"], 1))  # 출력: 2
print(getMinimumSize(["item1"], 1))  # 출력: -1
