def solution(numbers, K):
    answer = 0
    for i in range(len(numbers) -1):
        if abs(numbers[i] - numbers[i+1]) > K:
            for j in range(i+2, len(numbers) -1):
                if abs(numbers[i] - numbers[j]) > K:
                    j += 1
                elif abs(numbers[i] - numbers[j]) <= K:
                    numbers[i+1], numbers[j] = numbers[j], numbers[i+1]
                    answer += 1 
                elif answer == 0:
                    return -1
    return answer


numbers = [3, 7, 2, 8, 6, 4, 5, 1]
K = 3


print(solution(numbers, K))

