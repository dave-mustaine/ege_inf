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

# длинная арифметика
# https://education.yandex.ru/ege/task/39991489-2021-4ee7-96a1-f45152dbfcd2
def counterr():
    x = 0
    raznost = 0

    while raznost != 471:
        s = 9 ** 1_942 + 9 * 6 ** 971 + 214 - x
        s = abs(s)

        r = []

        while s > 0:
            r.append(s % 9)
            s //= 9

        raznost = abs(r.count(2) - r.count(8))

    return x


print(counterr())
