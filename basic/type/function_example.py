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

def print_n_time(value, n):
    for i in range(n):
        print(value)

print_n_time("Hello", 3)

def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "Hello", "Welcome", "~")
print()

def print_n_times(n, val, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "Hello", "Welcome", "~")


def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("Hello")
print()

def print_n_times(n=2, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(2, "Hello", "Welcome", "!")
print()

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(values)
        print()
print_n_times("Hello", "Welcome", "3", "4", n=3)
print_n_times("Hello", "Welcome", "3", n=3)

def test(a, b=10, c=100):
    print(a, b, c)

test(5, 4, c=60)
test(10, c=60)
test(10, b=60)
test(999)

def test(a=0, b=10, c=100):
    print(a, b, c)
test()

value = input("> ")
print(value)

def return_test():
    print("A")
    return
    print("B")
return_test()
print()

def return_test():
    return 100

value = return_test()
print(value)
print()

def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

print("1 to 10:", sum_all(1, 10))
print("1 to 10:", sum_all(1, 3))

def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

print("A :", sum_all(0, 100, 10))
print("A :", sum_all(0, 5, 3))
print("A :", sum_all(0, 5, 30))