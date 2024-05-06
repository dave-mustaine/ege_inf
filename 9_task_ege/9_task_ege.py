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

# lines = open('9_2.csv').readlines()  # 2. https://education.yandex.ru/ege/task/c51900be-b855-4ffb-97d5-8402bb52ffd8
#
# data = list()
# k = 0
#
# for line in lines:
#     line_ints = [int(number) for number in line.split(';')]
#     data.append(line_ints)
#
#     summs = [{line_ints[0] + line_ints[1], line_ints[2] + line_ints[3]},
#              {line_ints[0] + line_ints[2], line_ints[1] + line_ints[3]},
#              {line_ints[0] + line_ints[3], line_ints[1] + line_ints[2]}]
#
#     if (sum(line_ints) - max(line_ints)) > max(line_ints) and len(summs[0]) == 2 and len(summs[1]) == 2 and \
#             len(summs[2]) == 2:
#         k += 1
#
# print(k)

# lines = open('9_3.csv').readlines()  # 3. https://education.yandex.ru/ege/task/0a1c32bb-0828-47c8-bab2-035af95f4fa7
#
# data = list()
# k = 0
#
# for line in lines:
#     data.append([int(number) for number in line.split(';')])
#
# for data_set_ in data:
#     data_set_.remove(min(data_set_))
#     data_set_.remove(max(data_set_))
#
#     if (sum(data_set_) / 3) >= 8.0:
#         k += 1
#
# print(k)

# lines = open('9_4.csv').readlines()  # 4. https://education.yandex.ru/ege/task/d62dc568-941a-44da-870b-b8cc21faee9f
#
# data = list()
# counter = 0
#
# for line in lines:
#     data.append([int(number) for number in line.split(',')])
#
# for data_ in data:
#     data_odd = 0
#     data_even = 0
#
#     for x in data_:
#         if (x % 2) == 1:
#             data_odd += x
#         else:
#             data_even += x
#
#     if len(set(data_)) == 4 and not data_odd > data_even:
#         counter += 1
#     elif data_odd > data_even and len(set(data_)) != 4:
#         counter += 1
#
# print(counter)

# lines = open('9_5.csv').readlines()  # 5. https://education.yandex.ru/ege/task/a787ce29-0649-4566-a463-0869774a61dc
#
# data = list()
# counter = 0
#
# for line in lines:
#     data.append([number for number in line.split(',')])
#
# print(data)
#
# for data_line in data:
#     year_of_birth = int(data_line[0][-4::])
#     month_of_birth = int(data_line[1])
#     sex = data_line[3][0]
#
#     # print(year_of_birth, month_of_birth, sex)
#
#     if (year_of_birth % 4) == 0 and (year_of_birth % 100) != 0:
#         if sex == 'ж':
#             if month_of_birth == 10:
#                 counter += 1
#     elif (year_of_birth % 400) == 0:
#         if sex == 'ж':
#             if month_of_birth == 10:
#                 counter += 1
#
# print(counter)

# import math as m
# lines = open('9_6.csv').readlines()  # 6. https://education.yandex.ru/ege/task/2c9beda9-8bb0-497c-b6d3-d4fd322f0df0
#
# counter = 0
#
# for i in range(len(lines)):
#     data = [int(number) for number in lines[i].split(',')]
#
#     set_of_data = len(set(data))
#
#     square_of_summ = (min(data) + max(data)) ** 2
#
#     data.remove(min(data))
#     data.remove(max(data))
#
#     if square_of_summ > m.prod(data) and set_of_data == 5:
#         counter += (i + 1)
#
# print(counter)

# lines = open('9_7.csv').readlines()  # 7.
#
# counter = 0
# odd_number_counter = 0
#
# for line in lines:
#     data = [int(number) for number in line.split(',')]
#
#     len_of_data = len(set(data))
#
#     for number in data:
#         if number % 2 == 1:
#             odd_number_counter += 1
#
#     if (len_of_data < 6 and odd_number_counter != 3) or (len_of_data == 6 and odd_number_counter == 3):
#         counter += 1
#
# print(counter)

lines = open('9_8.csv').readlines()

counter = 0

for line in lines:
    data = [int(x) for x in line.split(';')]

    sum_of_data = sum(data)

