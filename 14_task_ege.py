# # длинная арифметика
# # https://education.yandex.ru/ege/task/83d644e9-902c-44d8-a9e5-d7f946811a29
# s = 7 ** 21 + 49 ** 13 - 7 ** 10
#
# r = []
#
# while s > 0:
#     r.append(s % 7)
#     s //= 7
#
# print(r.count(6))

# # выражение с неизвестными цифрами
# # https://education.yandex.ru/ege/task/660f09fb-51cc-496a-a57e-6aa856698de9
# for x in '0123456789abcde':
#     s = int('97968' + x + '13', 15) + int('7' + x + '213', 15)
#
#     if s % 11 == 0:
#         print(x)

# # длинная арифметика
# # https://education.yandex.ru/ege/task/062a4793-f5f9-4b96-be39-1a81c87197f3
# s = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50
#
# s = abs(s)
#
# r = []
#
# while s > 0:
#     r.append(s % 49)
#     s //= 49
#
# print(sum(r))

# # длинная арифметика
# # https://education.yandex.ru/ege/task/5b214f5e-974b-46db-bf04-5aa73d9d99d3
# s = 3 * 5 * 1_140 + 2 * 15 ** 1_025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
#
# s = abs(s)
#
# r = []
#
# while s > 0:
#     r.append(s % 15)
#     s //= 15
#
# maximums = []
# count = 1
#
# for i in range(len(r) - 1):
#     if r[i] == r[i + 1]:
#         count += 1
#     if r[i] != r[i + 1]:
#         maximums.append(count)
#         count = 1
#
# print(max(maximums))

# # длинная арифметика
# # https://education.yandex.ru/ege/task/12b3aabc-7777-4808-b29a-29993b289cca
# s = 3 * 3_125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2_024
# s = abs(s)
#
# r = []
#
# while s > 0:
#     r.append(s % 25)
#     s //= 25
#
# print(r.count(0))

# # длинная арифметика
# # https://education.yandex.ru/ege/task/c5e4d9a3-018f-4705-b0dc-68403da4763f
# s = 3 * 7 ** 82 - 4 * 49 ** 21 + 5 * 343 ** 25
#
# s = abs(s)
#
# r = []
#
# while s > 0:
#     r.append(s % 7)
#     s //= 7
#
# print(sum(r))

# # длинная арифметика РАЗОБРАТЬ
# # https://education.yandex.ru/ege/task/39991489-2021-4ee7-96a1-f45152dbfcd2
# def counterr():
#     x = 0
#     raznost = 0
#
#     while raznost != 471:
#         s = 9 ** 1_942 + 9 * 6 ** 971 + 214 - x
#         s = abs(s)
#
#         r = []
#
#         while s > 0:
#             r.append(s % 9)
#             s //= 9
#
#         raznost = abs(r.count(2) - r.count(8))
#
#     return x
#
#
# print(counterr())

# # выражение с неизвестными цифрами
# # https://education.yandex.ru/ege/task/e07ffce3-c3fb-4aad-933f-4291ee998760
# for x in '0123456789abcd':
#     for y in '0123456789abcd':
#         s = int('14' + y + '5' + x + '2', 14) + int('31' + x + '2' + y + '3', 14)
#
#         if s % 9 == 0:
#             print(x, y, s / 9)

# # выражение с неизвестными цифрами
# # https://education.yandex.ru/ege/task/749a92f0-0083-4931-90cf-8c987a48ed9c
# x_y = []
#
# for x in '0123456789abcdef':
#     for y in '0123456789abcdef':
#         s = int('27a' + x + '23', 16) + int('8' + y + 'e5d2', 16)
#
#         if s % 5 == 0:
#             x_y.append(int(x, 16) + int(y, 16))
#
# print(max(x_y))

# # выражение с неизвестными цифрами
# # https://education.yandex.ru/ege/task/376fdf5f-fe0f-49fe-873c-698126bf1ccd
#
# for x in '0123456789abcdefghijklmn':
#     for y in '0123456789abcdefghijklmn':
#         s = (int('4m' + x + 'f', 24) + int('265afdn' + x, 24) + int('n4' + x + '931b3l', 24)
#              + int('ng' + x + '4f', 24) + int('fkjb5' + x + 'ik', 24))
#
#         if s % 23 == 0:
#             print(s / 23)
#             break

# # выражение с неизвестными цифрами РАЗОБРАТЬ
# # https://education.yandex.ru/ege/task/376fdf5f-fe0f-49fe-873c-698126bf1ccd
# ss = []
# # int('4' + y, int(x))
# for x in '01234567':
#     for y in '01234567':
#         s = int('36' + x + '53', 8) - (4 * int(x) + int(y))
#         ss.append(s)
#
# print(min(ss))

# # выражение с неизвестными цифрами
# # https://education.yandex.ru/ege/task/efccf0c5-008f-4ac1-a586-9973538f9523
# ss = []
# for x in '0123456789abcdefghijklmno':
#     for y in '0123456789abcdefghijklmno':
#         s = int('b7' + x + '35f1', 25) + int('16' + x + 'k1', 25) + int('1' + x + 'g', 25)
#         if s % 24 == 0:
#             ss.append(s)
#
# print(max(ss) // 24)

# # выражение с неизвестными цифрами
# # https://education.yandex.ru/ege/task/258db83f-773f-43a0-88da-89f8e3c2ab70
# ss = []
# for x in '0123456789abcdefgh':
#     s = int('77968' + x + '11', 18) + int('4' + x + '213', 18)
#     if s % 7 == 0:
#         ss.append(x)
#
# print((int('77968' + max(ss) + '11', 18) + int('4' + max(ss) + '213', 18)) / 7)

# # длинная арифметика
# # https://education.yandex.ru/ege/task/1273d7d9-0226-4742-99da-70fc4876a4eb
# s = 7 * 5 ** 123 + 6 * 5 ** 111 - 5 * 25 ** 50 + 4 * 125 ** 30 - 3 * 5 ** 10
# s = abs(s)
#
# r = []
#
# while s > 0:
#     r.append(s % 5)
#     s //= 5
#
# print(r.count(4))

# # длинная арифметика
# # https://education.yandex.ru/ege/task/6e6c2557-26e8-4b87-a6ff-96defe05f178
# s = 5 ** 20 + 5 ** 10 - 5 ** 13 - 5 ** 3
#
# r = []
#
# while s > 0:
#     r.append(s % 5)
#     s //= 5
#
# print(sum(r))
