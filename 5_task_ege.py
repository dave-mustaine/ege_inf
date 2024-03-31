# R = 0
# numberr = 0
#
# while R < 76:
#     numberr += 1
#
#     n_bits = str(bin(numberr))[2::]
#
#     if not (numberr % 3):
#         n_bits = n_bits + n_bits[-3:]
#     else:
#         a = (numberr % 3) * 3
#         n_bits = n_bits + str(bin(a))[2::]
#
#     R = int(n_bits, 2)
#
# print(numberr - 1)

# import math
#
# n = 1000
# R = 0
# N = list()
#
# while R < 85:
#     nn = str(n)
#
#     for i in nn:
#         N.append(int(i))
#
#     ii = max(N)
#     iii = min(N)
#
#     first_of_r = str(ii + iii)
#
#     N.remove(ii)
#     N.remove(iii)
#
#     second_of_r = str(math.prod(N))
#
#     R = int(first_of_r + second_of_r)
#
#     print(n, R)
#
#     n += 1

# a = 5 ** 6
# b = (5 ** 5) * 4
# c = (5 ** 4) * (4 ** 2)
# d = (5 ** 3) * (4 ** 3)
# e = (5 ** 2) * (4 ** 4)
# f = 5 * (4 ** 5)
# g = (5 ** 2) * (4 ** 4)
# h = (5 ** 3) * (5 ** 2)
# i = (5 ** 4) * (4 ** 2)
# j = (5 ** 2) * (4 ** 4)
# k = (5 ** 3) * (4 ** 3)
# l = (5 ** 2) * (4 ** 4)
# m = (5 ** 3) * (4 ** 3)
# n = (5 ** 4) * (4 ** 2)
#
# print(a + b + c + d + e + f + g + h + i + j + k + l + m + n)

n = 0
R = 0

while R < 109:
    n += 1
    n_6 = list()

    while n > 0:
        n_6.append(n % 6)
        n //= 6

    zeros = n_6.count(0)
