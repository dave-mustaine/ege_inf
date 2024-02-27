# 27-1 (server -> Задания -> ЕГЭ2024)
file_1 = open('27-A1.txt').readlines()
file_2 = open('27-B1.txt').readlines()

n1 = int(file_2[0])
data = []

for text in file_2[1:]:
    data.append(sorted([int(i) for i in text.split()]))

s = 0
min_d = 0

for i in data:
    s += i[0]
    if i[1] - i[0] % 10:
        min_d = min(i[1] - i[0], min_d)

print(s)
