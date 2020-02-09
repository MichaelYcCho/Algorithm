s = 0
for i in list(range(21)):
    print(f"i값 {i}")
    for j in str(i):
        print(f"j값은 {j}")
        s += int(j)
        print(f"값 s: {s}")
        
print(s)
