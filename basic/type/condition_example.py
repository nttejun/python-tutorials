
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

print("가나" < "다라")
print("1" < "10")

condition_x = 10
condition_a = condition_x < 20
print("condition_a : ",condition_a)

if 10 % 2 == 0:
    print("10 % 2 TRUE")


if 10 % 2 == 1:
    print("10 % 2 FALSE")
else:
    print("10 % 2 == 0")


if 5 % 2 == 0:
    print("5 % 2 == 0")
elif 5 % 2 == 2:
    print("5 % 2 == 2")
elif 5 % 2 == 1:
    print("5 % 2 == 1")
else:
    print("5 % 2 == else")

if 2 == 2:
    pass
elif 1 == 1:
    print("1 == 1")
else:
    print("else")

if 5+5 == 10:
    print("NotImplementedError Exception 발생")
    raise NotImplementedError
else:
    raise NotImplementedError