with open('27986_A.txt') as file_:
    text = list(map(int, file_.readlines()))

data = sorted(text)[::-1]

a = 1
b = 1

for i in data:
    if i % 7 == 0 and not i % 49 == 0:
        a = i
        break

for i in data:
    if not i % 7 == 0:
        b = i
        break

print(a * b)
