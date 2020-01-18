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

