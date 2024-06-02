# from itertools import product
#
# c = 0
#
# for i1, i2, i3, i4, i5, i6 in product([0, 1, 2, 3, 4], repeat=6):
#     f = str(i1) + str(i2) + str(i3) + str(i4) + str(i5) + str(i6)
#     if f.count('0') == 3:
#         c += 1
# print(c)

c = 0  # https://education.yandex.ru/ege/task/93ac0c3b-ddee-4791-a179-b256cda73ea2

for i1 in range(5):
    for i2 in range(5):
        for i3 in range(5):
            for i4 in range(5):
                for i5 in range(5):
                    for i6 in range(5):
                        f = str(i1) + str(i2) + str(i3) + str(i4) + str(i5) + str(i6)
                        if f.count('0') == 3:
                            c += 1

print(c)
