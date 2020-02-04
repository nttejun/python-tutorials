def input_number_fun_a():
    print("함수가 호출되었습니다")


input_number_fun_a()
print()

print(input_number_fun_a())
print()

def input_number_fun_b(num):
    print("전달받은 숫자는 : {} 입니다".format(num))
    print("전달받은 숫자는 :", num,"입니다.")

input_number_fun_b(5)
print()

def input_number_fun_c(value, n):
    for i in range(n):
        print(value)


input_number_fun_c("안녕하세요", 5)
print()