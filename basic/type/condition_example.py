
if True:
    print("True 화인1")
    print("True 화인2")

if False:
    print("False 확인1")
    print("False 확인2")


a_val = 10
if a_val!=10:
    print("10 맞습니다")

a_val = 10
if a_val==10:
    print("10 맞습니다")

b_val = int(0)
if b_val == 0:
    print("0입니다.")
if b_val < 10:
    print("10보다 작습니다.")
if b_val > 10:
    print("10보다 큽니다.")

import datetime
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.second, "초")

now = datetime.datetime.now()

print("{}년 {}월 {}일 입니다".format(
    now.year,
    now.month,
    now.day
))

date_format = "현재 {}년 {}월 {}일 입니다".format(
    now.year,
    now.month,
    now.day
)
print(date_format)

if now.hour < 12:
    print("현재 시간은 12시 이전이다")
else:
    print("현재 시간은 12시 이후이다")


if now.month >= 1 or now.month <= 3:
    print("{}월로 봄입니다.".format(now.month))
