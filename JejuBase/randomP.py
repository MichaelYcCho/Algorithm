import random as r

print(1, r.randint(1, 100))
print(2, r.random())
print(3, r.uniform(1, 10))
print(4, r.randrange(1, 10, 2))


l = [i for i in range(10)]
print(r.choice(l))
print(r.sample(l, 5))
r.shuffle(l)
print(l)
