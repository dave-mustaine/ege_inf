# # https://education.yandex.ru/ege/task/51046c4b-dbc1-444a-bff0-4827db0d36fe
# data = [int(number) for number in open('17_1.txt').readlines()]
#
# max_divided_by_21 = 0
#
# for num in data:
#     if num % 21 == 0 and num > max_divided_by_21:
#         max_divided_by_21 = num
#
# counter = 0
# pairs = []
#
# for i in range(len(data) - 1):
#     if data[i] > max_divided_by_21 or data[i + 1] > max_divided_by_21:
#         counter += 1
#         pairs.append(data[i] + data[i + 1])
#
# print(counter, min(pairs))

# # https://education.yandex.ru/ege/task/6e42c9ec-fd34-40c3-a695-96e205bc6beb
# data_ints = [int(number) for number in open('17_2.txt').readlines()]
# data_lens = []
# summs_of_datas = []
#
# max_three_digit_number = 0
#
# for num in data_ints:
#     data_lens.append(len(str(num)[1:]) if num < 0 else len(str(num)))
#
#     if 99 < num < 1_000 and num > max_three_digit_number:
#         max_three_digit_number = num
#
# counter = 0
#
# for i in range(len(data_ints) - 1):
#     if (data_ints[i] + data_ints[i + 1]) <= max_three_digit_number:
#         if data_lens[i] == 3 and data_lens[i + 1] != 3:
#             summs_of_datas.append(data_ints[i] + data_ints[i + 1])
#             counter += 1
#         elif data_lens[i] != 3 and data_lens[i + 1] == 3:
#             summs_of_datas.append(data_ints[i] + data_ints[i + 1])
#             counter += 1
#
# print(counter, max(summs_of_datas), max_three_digit_number)

# https://education.yandex.ru/ege/task/525fcbaa-ca74-4f79-af9c-90a644e1cfc1
data_strs = [open('17_3.txt').readlines()]
data_ints = [int(number) for number in open('17_3.txt').readlines()]

data_threes = []

max_number_18 = 0

for num in data_strs:
    data_threes.append(1 if '3' in num else 0)
