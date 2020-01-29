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

for i in list_e:
    print("출력 : ", list_e[i-1])