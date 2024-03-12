# # https://education.yandex.ru/ege/task/2b1c56d7-cc00-456d-b644-5a9c5c3bcabc
# def tree(x, y, h=0):
#     if x + y >= 231 and h == 2:
#         return True
#     if x + y >= 231 and h != 2:
#         return False
#     if h > 2:
#         return False
#     if h % 2 == 0:
#         return tree(x + 4, y, h + 1) or tree(x, y + 4, h + 1) or\
#             tree(x * 3, y, h + 1) or tree(x, y * 3, h + 1)
#     else:
#         return tree(x + 4, y, h + 1) or tree(x, y + 4, h + 1) or\
#             tree(x * 3, y, h + 1) or tree(x, y * 3, h + 1)
#
#
# for m in range(1, 218):
#     if tree(10, m):
#         print(m)

# # https://education.yandex.ru/ege/task/2f365516-86fc-4f33-939c-e7df34f2f2bc
# def tree(x, y, h=0):
#     if x * y >= 123 and h == 2:
#         return True
#     if x * y >= 123 and h != 2:
#         return False
#     if h > 2:
#         return False
#     if h % 2 == 0:
#         return tree(x + 2, y, h + 1) or tree(x, y + 2, h + 1) or\
#             tree(x * 2, y, h + 1) or tree(x, y * 2, h + 1)
#     else:
#         return tree(x + 2, y, h + 1) or tree(x, y + 2, h + 1) or\
#             tree(x * 2, y, h + 1) or tree(x, y * 2, h + 1)
#
#
# for m in range(1, 41):
#     if tree(3, m):
#         print(m)

import math
a = []


def tree(x, y, h=0):
    if x + y <= 46 and h in (1, 3):
        return True
    if x + y <= 46 and h in (1, 3):
        return False
    if h > 3:
        return False
    if h % 2 == 0:
        return tree(x - 2, y, h + 1) or tree(x, y - 2, h + 1) or\
            tree(math.ceil(x / 2), y, h + 1) or tree(x, math.ceil(y / 2), h + 1)
    else:
        return tree(x - 2, y, h + 1) and tree(x, y - 2, h + 1) and\
            tree(math.ceil(x / 2), y, h + 1) and tree(x, math.ceil(y / 2), h + 1)


for m in range(26, 10_000):
    if tree(20, m):
        a.append(m)

print(a)


def tree1(x, y, h=0):
    if x + y <= 46 and h == 1:
        return True
    if x + y <= 46 and h == 1:
        return False
    if h > 3:
        return False
    if h % 2 == 0:
        return tree(x - 2, y, h + 1) or tree(x, y - 2, h + 1) or\
            tree(math.ceil(x / 2), y, h + 1) or tree(x, math.ceil(y / 2), h + 1)
    else:
        return tree(x - 2, y, h + 1) and tree(x, y - 2, h + 1) and\
            tree(math.ceil(x / 2), y, h + 1) and tree(x, math.ceil(y / 2), h + 1)


for m in range(26, 10_000):
    if tree(20, m):
        a.remove(m)

print(a)
