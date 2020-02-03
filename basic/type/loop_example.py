list_a = [1, 2, 3, 4]
print(list_a[0])
print(list_a[1:3])

list_a[2] = "3번"
print(list_a)
print(list_a[-1:2])
print(list_a[-2])
print(list_a[-2][0])

list_b = [[1,2], [1,3], [1,4], [1,5], [1,6]]
print(list_b[0])
print(list_b[0][1])
print(list_b)
print(len(list_b))
print(len(list_b[0]))

list_b.append([1,7])
print(list_b)

list_b[0].append(3)
print(list_b)

list_c = [1, 2, 3]
list_c.append(4)
list_c.append(5)
list_c.insert(0, 3)
print(list_c)

list_c.extend(list_b)
print(list_c)

list_d = list_a + list_b
print(list_a)
print(list_b)
print(list_d)


print(list_a)
del list_a[0]
print(list_a)

list_a[0] = 1
print(list_a)

list_a.pop(0)
print(list_a)

list_a.insert(0, 1)
list_a.insert(1, 2)
list_a.insert(2, 3)
list_a.insert(3, 4)
print(list_a)

del list_a[:2]
print(list_a)

list_a.remove("3번")
print(list_a)

list_a.clear()
print(list_a)

list_e = [10, 20, 30, 40, 50]
print(20 in list_e)
print(20 not in list_e)

for i in range(5):
    print("출력 : ", i)

list_f = {"가": 1,
          "나": 2}
print(list_f)
print(list_f["나"])

list_f = {"가나": ['가', '나'], "다라": ["다", "라"]}
print(list_f)
print(list_f["가나"])

dictionary = {
    "name": "여름과일",
    "type": "건조",
    "ingredient": ["바나나", "망고", "파일애플"],
    "origin": "korea"
}

print("dictionary : ", dictionary)
print("name : ", dictionary["name"])
print(dictionary["ingredient"][0])
dictionary["name"] = "가을과일"
print("name : " + dictionary["name"])

name = "망고"
dictionary_a = {
    name: "건조 망고",
    type: "반건조"
}
print(dictionary_a)

name = "망고"
type = "건조"
dictionary_b = {
    name: "건조 망고",
    type: "반건조"
}
print(dictionary_b)

dictionary_b["etc"] = "기타 메모"
print(dictionary_b)
del dictionary_b["etc"]
print(dictionary_b)

if "etc" in dictionary_b:
    print("etc 키가 존재합니다")
else:
    print('etc 키가 없습니다')

print(dictionary_b.get("없는 키"))
print(dictionary_b.get(type))
print(dictionary_b.get("type"))

for key in dictionary_b:
    print("key : ", key, "and", key)


range_a = range(5)
print(range_a)

range_b = range(1, 5)
print(range_b)

print(list(range_a))
print(list(range_b))

range_c = range(2, 5, 10)
print(range_c)
print(list(range_c))

range_d = range(0, 10 + 1)
print(range_d)
print(list(range_d))

range_e = range(0, 10, 2)
print(range_e)
print(list(range_e))

range_f = range(1, 20, 3)
print(range_f)
print(list(range_f))

range_g = range(1, 20, -3)
print(range_g)
print(list(range_g))

range_hh = 20
range_h = range(1, int(range_hh / 2))
print(list(range_h))

range_h = range(1, range_hh // 2)
print(list(range_h))

for i in range(5):
    print(str(i) + " 변수 ")
print()

range_array_a = [10, 20, 100, 200]
for i in range(len(range_array_a)):
    print("{}번째 반복 : {}".format(i, range_array_a[i]))

for i in range(4, 0 -1, -1):
    print("현재 반복 변수 : {}".format(i))
    print("현재 반복 변수 : {}, {}".format(i, i))

range_array_b = [1, 10, 50, 100, 150]
for element in range_array_b:
    print(element)


range_array_c = [1, 10, 50, 100, 150]
for i in range(len(range_array_c)):
    print("{}번째 반복 : {}".format(i, range_array_c[i]))

for i in range(4, 0-1, -1):
    print("현재 반복 변수 : {}".format(i))

for i in range(4, 0-1, -2):
    print("현재 반복 변수 : {}".format(i))

print()

for i in reversed(range(5)):
    print("현재 반복 변수 : {}".format(i))

print()


while_a = 0
while while_a < 10:
    print("{}번째 반복입니다.".format(while_a))
    while_a += 1

list_aa = [1, 2, 1, 2]
value = 2
while value in list_aa:
    list_aa.remove(value)
print(list_aa)

import time
print(time.time())

number_a = 0
target_a = time.time() + 2
while time.time() < target_a:
    number_a += 1

print("2초 동안 {}번 반복.".format(number_a))
print()

number_a = 0
while True:
    print("{}번째 반복문입니다.".format(i))
    number_a = number_a + 1
    input_a = input("> 종료하시겠습니까?(y): ")
    if input_a in ["y", "Y"]:
        print("반복문을 종료합니다")
        break

number_b = [5, 15, 6, 16, 7, 17]
for number in number_b:
    if number < 10:
        continue

print(number)
print()

for number in number_b:
    if number < 10:
        continue

print(number)
print()

list_g = [1, 10, 2, 20, 3, 30]
print(max(list_g))
print(sum(list_g))
print(reversed(list_g))
print(list_g[::-1])
print(list_g[::1])
print(list_g[::2])
print()

reversed_a = [1, 2, 3, 4, 5]
print(list(reversed(reversed_a)))

for i in reversed(reversed_a):
    print(" - ", i)

for i in reversed(reversed_a):
    print(" - {} - ".format(i))

list_aaa = ["A", "B", "C", "D"]
print(enumerate(list_aaa))
print(list(enumerate(list_aaa)))

item_a = {
    "KEY A" : "KEY A",
    "KEY B" : "KEY B",
    "KEY C" : "KEY C"
}

print("딕셔너리 items() 함수")
print("items : ", item_a.items())

for key, element in item_a.items():
    print("dictionary [{}] = {} ".format(key, element))

array_a = []
for i in range(0, 20, 2):
    array_a.append(i * 1)

print(array_a)

array_a = [i*i for i in range(0, 20, 2)]
print("리스트 내포 : [표현식 for 반복자 in 반복할 수 있는 것]")
print(array_a)

array_b = ["사과", "딸기", "배", "초콜릿"]
array_c = [fruit for fruit in array_b if fruit != "초콜릿"]
print("[표현식 for 반복자 in 반복할 수 있는 것 if 조건문] =", array_c)

number_c = int(input("정수 입력 > "))
print_a = (
    "여러 줄 "
    "하나의 문자열로 "
    "연결되어 생성 "
)
if number_c % 2 == 0:
    print("""\
    구문 내부에
    여러 줄 문자열
    사용하는 경우 문제점
    {} = 짝수""".format(number_c, number_c))
    print("구문 내부에\n여러 줄 문자열 사용하는 경우 올바른 케이스\n{} = 짝수".format(number_c, number_c))
    print()
    print(print_a)
else:
    print("""\
    {} = 홀수""".format(number_c, number_c))
    print("구문 내부에\n여러 줄 문자열 사용하는 경우 올바른 케이스\n{} = 홀수".format(number_c, number_c))
    print()
    print(print_a)


print()
print("::".join(["1", "2", "3", "4", "5"]))
join_a = ["1", "2", "3", "4", "5"]

number_d = int(input("정수 입력 >"))
if number_d % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]).format(number_d, number_d))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number_d, number_d))

number_e = [1, 2, 3, 4, 5, 6]
number_f = reversed(number_e)
print("reversed numbers :", number_f)
print(next(number_f))
print(next(number_f))
print(next(number_f))
print(next(number_f))
print(next(number_f))
print(next(number_f))

print()
print("{:o}".format(10))
print("{:x}".format(10))
print(int("12", 6))
print(int("10", 16))
print(int("a", 16))
