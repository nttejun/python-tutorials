import keyword
print(keyword.kwlist)
print(52)
print("")
print("test")
print('test')
print()
print(type("test"))
print("'test'입니다")
print("\"test\"입니다")
print("사는 곳\t나이\t이름\t사는곳\t경기도고양시\t이상")
print("가\t가나\t가나다\t가나다라\t가나다라마\t가나다라마바")
print("\\ \\ \\ \\ \\")
print(
"""이름
나이
사는곳"""
)
print(
"""\
이름
나이
사는곳\
"""
)
print(
"""
이름
나이
사는곳
"""
)
print("3회 반복\n" * 3)
print("테스트"[0])
print("테스트"[1])
print("테스트"[2])
print("테스트"[-1])
print("테스트"[-2])
print("테스트"[-3])
print("파이썬연습"[0:1])
print("파이썬연습"[2:3])
print("파이썬연습"[2:4])
print("테스트".split("스"))
print(len("파이썬연습"))

print("3 + 5 : ", 3+5)
print("3 / 2 : ", 3/2)
print("3 / 2 : ", 7/2)
print("3 / 2 : ", 3//2)
print(" 3 ** 3 : ", 3**3)
print(" 3*3 : ", 3*3)
print(" (3+5)*10 : ", (3+5)*10 )

String = input("Welcome : ")
string = input("Welcome : ")
str = input("Welcome: ")

print(String)
print(string)
print(str)
print(type(str))
print(type(String))
print(type(string))

number = input("number : ")
num = input()
print(number)
print(type(number))
print(type(num))

string_a = input("입력 : ")
int_a = int(string_a)
print(type(int_a))

string_b = input("입력 : ")
float_b = float(string_b)
print(type(float_b))

format_a = "Python {} ".format(5000)
format_b = "{} {} {}".format(10, 20, 30)
format_c = "{} {} {}".format("가", "나", "다")
print(format_a)
print(format_b)
print(format_c)
output_a = "{:10d}".format(50)
output_b = "{:-10d}".format(50)
output_c = "{:+10d}".format(-50)
output_d = "{:-10d}".format(-50)
output_f = "{:+4d}".format(50)
output_g = "{:-4d}".format(50)
output_h = "{:+04d}".format(+50)
output_i = "{:-04d}".format(+50)
output_j = "{:=+04d}".format(-50)
output_k = "{:=-04d}".format(-50)
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print(output_j)
print(output_k)

float_aa = "{:15f}".format(52)
float_bb = "{:15.3f}".format(52)
float_cc = "{:15.3f}".format(52.2)
float_dd = "{:15.3f}".format(52.23455)
float_ee = "{:g}".format(52.00)
float_ff = "{:g}".format(52.2350)
float_gg = "{:g}".format(52.255)
print(float_aa)
print(float_bb)
print(float_cc)
print(float_dd)
print(float_ee)
print(float_ff)
print(float_gg)

sentence_a = """
    문자열
    함수
    호출
"""
print(sentence_a)
print(sentence_a.strip())

isCheck_a = "test"
print("isCheck : ".isalnum())
print("isCheck  ".isalnum())
print("isCheck".isalnum())
print("-1".isdecimal())
print("-1".isdigit())
print("isCheck ! @ ".isdecimal())
print(isCheck_a.isidentifier())
print("3".isdecimal())
print("3".isdigit())

find_a = "테스트케이스".find("스")
find_b = "테스트케이스".find("가")
find_c = "테스트케이스".rfind("스")
print(find_a)
print(find_b)
print(find_c)

in_a = "테스트케이스" in "가나다"
in_b = "테스트케이스" in "테스"
print(in_a)
print(in_b)
print("테스트케이스" in "테스트")

in_c = "가나다" in "테스트케이스"
in_d = "테스" in "테스트케이스"
print(in_c)
print(in_d)
print("테스트" in "테스트케이스")

split_a = "테 스 트 케 이 스".split(" ")
print(split_a)

print(not True)
print(not False)

under_num = 10
print("under_num:", under_num)
print("under_num", under_num)
print("not under_num", not under_num)

print("치킨", "치킨" or "배달")
print("치킨", "치킨" and "배달")

discount = "치킨" or "피자"
print(discount, "치킨")
print(discount, "짜장면")
print("치킨", discount)
print("짜장면", discount)