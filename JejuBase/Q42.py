#달력문제

import datetime

m = int(input())
d = int(input())

def findDay(m, d):
    day = ["일", "월", '화', "수", "목", "금", "토"]
    return day[datetime.date(2020, m, d).weekday()]



print(findDay(m, d))