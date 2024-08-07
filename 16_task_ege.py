# import sys
# from functools import lru_cache
#
# sys.setrecursionlimit(1_000_000_000)
#
#
# # number = 0
# # func = 0
# # number_of_zeros = 0
#
#
# @lru_cache
# def f(n):
#     if n > 0 and (not n % 2):
#         return n
#     elif n > 0 and (n % 2):
#         return f(n - 1)
#
#
# # while func != 34:
# #     func = f(number)
# #     number += 1
#
# print(f(11))
# # for i in range(number, 6000):
# #     n = i
# #     while True:
# #         n = (n / 6 - 2) / 6
# #         print(i)
#

# import sys
# from functools import lru_cache
# from decimal import Decimal
#
# sys.setrecursionlimit(1_000_000_000)
#
#
# @lru_cache
# def f(n):
#     if n <= Decimal('1'):
#         return Decimal('0.5')
#     elif n > Decimal('1'):
#         return (n + Decimal('1')) * f(n - Decimal('1'))
#
#
# print(f(Decimal('200')) / f(Decimal('198')))

# import sys
# from functools import lru_cache
#
# sys.setrecursionlimit(1_000_000_000)
#
#
# @lru_cache
# def f(n):
#     if n < 3:
#         return 2
#     elif n > 2 and (n % 2):
#         return 2 * f(n - 1) - f(n - 2) - 2
#     else:
#         return 2 * f(n - 2) - f(n - 1) + 2
#
#
# print(f(17))

import sys
from functools import lru_cache

sys.setrecursionlimit(1_000_000_000)


@lru_cache
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * f(n - 1)


print((f(2024) - f(2023)) / f(2022))
