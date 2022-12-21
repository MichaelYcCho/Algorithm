STR1 = ["h", "e", "l", "l", "o"]
STR2 = ["H", "a", "n", "n", "a", "h"]

def reverse_string(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
    
    return s

print(reverse_string(STR1))
print(reverse_string(STR2))



def reverse_string2(s: list[str]) -> None:
    s.reverse()
    return s

print(reverse_string2(STR1))