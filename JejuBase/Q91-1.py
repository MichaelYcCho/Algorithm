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

total_average = 0
c_average = []
s_average = 0

for c in total_score:
    for s in c:
        s_average += sum(s)/5
    c_average.append(s_average // 30)
    s_average = 0

print(c_average)
print(sum(c_average)//7)  # 클래스 전체평균 


''' numpy사용
a = np.array(total_score)
print(a.shape) # 7개의 클래스 30명의 학생 5개의 점수 
# a.size 전체사이즈 

# 30개의 리스트를 더하는법



'''