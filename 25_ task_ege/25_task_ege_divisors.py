# 1. https://education.yandex.ru/ege/task/fd10b825-4786-452a-92b6-6c74774db1e0
for i in range(321_655, 654_322, 2):
    ks = set()
    f = 1

    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0 and j % 2:
            ks.add(j)
            ks.add(int(i / j))
        if i % j == 0 and j % 2 == 0:
            f = 0
            break
        if len(ks) > 70:
            print(i, max(ks))
            break
