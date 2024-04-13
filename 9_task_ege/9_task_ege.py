# t = open('9_1.csv').readlines()  # 1. https://education.yandex.ru/ege/task/cecbe39b-e6f6-479b-b23b-b0261ac504fe
#
# data = list()
# k = 0
#
# for i in t:
#     stroka = [int(j) for j in i.split(',')]
#     data.append(stroka)
#     f = 1
#
#     for j in stroka:
#         if stroka.count(j) > 2:
#             f = 0
#
#     if len(set(stroka)) == 5 and f and ((sum(stroka) - sum(set(stroka))) / 2) < (sum(stroka) / 7):
#         k += 1
#
# print(k)

lines = open('9_2.csv').readlines()  # 2. https://education.yandex.ru/ege/task/c51900be-b855-4ffb-97d5-8402bb52ffd8

data = list()
k = 0

for line in lines:
    line_ints = [int(number) for number in line.split(';')]
    data.append(line_ints)

    summs = [{line_ints[0] + line_ints[1], line_ints[2] + line_ints[3]},
             {line_ints[0] + line_ints[2], line_ints[1] + line_ints[3]},
             {line_ints[0] + line_ints[3], line_ints[1] + line_ints[2]}]

    if (sum(line_ints) - max(line_ints)) > max(line_ints) and len(summs[0]) == 2 and len(summs[1]) == 2 and\
        len(summs[2]) == 2:
        k += 1

print(k)
