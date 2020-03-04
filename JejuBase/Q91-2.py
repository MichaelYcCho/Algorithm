import random as r
import numpy as np

student_score = []
class_score = []
total_score = []

for k in range(7):
    class_score = []
    for j in range(30):
        student_score = []
        for i in range(5):
            student_score.append(r.randint(1, 100))
        class_score.append(student_score)
    total_score.append(class_score)


#print(len(total_score))

a = np.array(total_score)
#print(a)
b = np.sum(a, axis=2)  # axis=2 2차원 (해당 행(row)을 더함)

c = b/5
d = np.sum(c, axis=1) 
print(d/30) #반평균점수


''' numpy사용

print(a.shape) # 7개의 클래스 30명의 학생 5개의 점수 
# a.size 전체사이즈 

# 30개의 리스트를 더하는법



'''