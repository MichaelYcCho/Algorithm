logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

def rerderLogFiles(logs: list[str]) -> list[str]:
    str_log, num_log = [], []

    for l in logs:
        if l.split()[1].isdigit(): # 구현부 정수여부 체크
            num_log.append(l)
        else:
            str_log.append(l)

    str_log.sort(key=lambda x : (x.split()[1:], x.split()[0]))

    return str_log + num_log


print(rerderLogFiles(logs))