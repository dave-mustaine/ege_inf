# def f(a, b):
#     if a == 10:
#         return 0  # если не заходить в точку
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         return f(a + 1, b) + f(a * 2, b)
#
#
# print(f(1, 28))


# def f(a, b):
#     # if a == 10:
#     #     return 0  # если не заходить в точку
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         return f(a + 1, b) + f(a * 2, b)
#
#
# print(f(1, 10) * f(10, 20))


# def f(a, b):
#     if a == 11:
#         return 0  # если не заходить в точку
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         return f(a + 1, b) + f(a * 2, b)
#
#
# print(f(1, 10) * f(10, 20))


# def variations(a, b):  # https://education.yandex.ru/ege/task/237b7023-9d4e-4268-a733-b7e1d23ff11b
#     if a == 20:
#         return 0
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         return variations(a + 1, b) + variations(a + 2, b) + variations(a * 3, b)
#
#
# print(variations(4, 10) * variations(10, 22))

# import sys
#
# sys.setrecursionlimit(1_000_000_000)


# def variations(a, b):  # https://education.yandex.ru/ege/task/1c5e34f0-e4fa-4d36-b02c-a35b4daadb74
#     if a == 50:
#         return 0
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         a1 = variations(a + 3, b)
#         a2 = variations(2 * a + 1, b)
#         a3 = variations(a + (a % 3), b)
#         return a1 + a2 + a3
#
#
# print(variations(5, 23) * variations(23, 89))


# def variations(a, b):  # https://education.yandex.ru/ege/task/7f35c6c9-51a5-4f54-bd42-92f9c15ff6af
#     if a == 27:
#         return 0
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         return variations(a + 1, b) + variations(a * 2, b) + variations(a * 3, b)
#
#
# print(variations(5, 9) * variations(9, 43))


# def variations(a, b):  # https://education.yandex.ru/ege/task/1e0cb6b4-4bc0-4443-bd23-71dbb3d80d36
#     if a == 15:
#         return 0
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         return variations(a + 1, b) + variations(a * 2, b) + variations(a * 3, b)


# print(variations(1, 11) * variations(11, 25))


# def variations(a, b):  # https://education.yandex.ru/ege/task/66370f14-aa4b-4640-8dca-e03c6c4386bf
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         return variations(a + 1, b) + variations(a + 2, b) + variations(a * 3, b)
#
#
# print(variations(6, 15) * variations(15, 25) + variations(6, 21) * variations(21, 25) -
#       2 * variations(6, 15) * variations(15, 21) * variations(21, 25))


# def variations(a, b):  # https://education.yandex.ru/ege/task/fc7ab1b0-2ae1-4379-9e30-36ebb7b1683f
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         return variations(a + 1, b) + variations(a * 2, b) + variations(a * 3, b)
#
#
# s = 0
# for i in range(2, 15, 2):
#     s += variations(i, 15)
#
# print(s)


# def variations(a, b):  # https://education.yandex.ru/ege/task/5cabc1d6-16ab-44fe-a8c2-b55922553fa5
#     if a == b:
#         return 1
#     if a < b:
#         return 0
#     if a > b:
#         return variations(a - 2, b) + variations(a - 5, b)
#
#
# print(variations(24, 3))


def variations(a, b):  # https://education.yandex.ru/ege/task/5cabc1d6-16ab-44fe-a8c2-b55922553fa5
    if a == 8:
        return 0
    if a == b:
        return 1
    if a < b:
        return 0
    if a > b:
        return variations(a - 2, b) + variations(a // 2, b)


print(variations(70, 22) * variations(22, 5))
