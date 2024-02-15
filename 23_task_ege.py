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


def f(a, b):
    if a == 11:
        return 0  # если не заходить в точку
    if a == b:
        return 1
    if a > b:
        return 0
    if a < b:
        return f(a + 1, b) + f(a * 2, b)


print(f(1, 10) * f(10, 20))
