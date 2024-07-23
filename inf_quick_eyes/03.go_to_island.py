# 배 운영시간 : 09 ~ 21 (12시간)
# 한시간에 100명씩, 12시간 -> 1200명, 하루 1200명 운송가능
waiting_people = 14000605

# 대기일 = 대기인원 // 1200 = 11667
waiting_day = waiting_people // 1200  # 11667일 대기해야함


day_of_year = 0  # 일년 일수
for i in range(10, 0, -1):
    day_of_year += 2**i  # 2046


# (남은 년 = 대기일 // 일년 일수 = 5
# (남은 일수 = 대기일 % 일년 일수 = 1437
# => 즉 5년 1437일 남음
remain_year = waiting_day // day_of_year  # 5
remain_day = waiting_day % day_of_year  # 1437


month_to_day = 0  # 월별 일수 누적값
month = 0

for i in range(10, 0, -1):
    calc_day = month_to_day
    month_to_day += 2**i
    month += 1
    if (month_to_day) > remain_day:
        break

aboard_day = remain_day - calc_day  # 413 -> 즉 2월의 413번째 날에 탑승가능


# 최종 남은 인원 (마지막날 남은 인원) = 대기인원 % 1200(하루 수용량)
last_day_waiting_people = waiting_people % 1200
print(last_day_waiting_people)
