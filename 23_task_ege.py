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


nums = set()


# def variations(a, b):  #
#     if a % 2 == 1 and a < 100:
#         nums.add(a)
#     if a == b:
#         return 1
#     if a > b:
#         return 0
#     if a < b:
#         return variations(a + 3, b) + variations(a * 3, b)
#
#
# print(variations(10, 100))
# print(len(nums))
