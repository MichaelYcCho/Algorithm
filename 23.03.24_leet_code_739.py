# https://leetcode.com/problems/daily-temperatures/
# 10^5 -> O(n^2) 으로는 풀지말라는 뜻이다.


def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        # cur_temp 보다 온도가  (stack의 마지막 원소) 낮으면 pop
        while stack and stack[-1][1] < cur_temp:
            prev_day, prev_temp = stack.pop()
            result[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
