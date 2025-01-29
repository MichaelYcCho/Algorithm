def solution(myString, pat):
    return int(pat.lower() in myString.replace("A", "b").replace("B", "a"))


def solution(myString, pat):
    pat = list(pat)
    for i in range(len(pat)):
        if pat[i] == "B":
            pat[i] = "A"
        else:
            pat[i] = "B"
    if "".join(pat) in myString:
        return 1
    return 0
