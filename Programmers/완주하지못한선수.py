def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        print(f"i {i}, j {j}")
        if i != j:
            return i

    return participant[-1]
        


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))


