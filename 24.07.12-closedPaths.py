def closedPaths(number):
    closed_path_counts = {"0": 1, "4": 1, "6": 1, "9": 1, "8": 2}
    total_closed_paths = 0

    for digit in str(number):
        if digit in closed_path_counts:
            total_closed_paths += closed_path_counts[digit]

    return total_closed_paths


# 예제 테스트
print(closedPaths(630))  # 출력: 2
print(closedPaths(1288))  # 출력: 4
