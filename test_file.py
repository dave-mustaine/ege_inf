# N = int(input())
#
# primes = [i for i in range(N + 1)]
#
# primes[1] = 0
#
# i = 2
#
# while i <= N:
#     if primes[i] != 0:
#         j = i + i
#         while j <= N:
#             primes[j] = 0
#             j = j + i
#     i += 1
#
# primes = [i for i in primes if i != 0]
#
# print(sum(primes))

# lines = '''25 K Igor
# 11 E Kirill
# 15 B Anna
# 20 E Igor
# 7 E Anna
# 13 E Kirill
# 21 E Anna
# 33 K Ivan
# 17 E Kirill
# 20 E Anna'''.split('\n')
#
# drivers = list()
# salaries = list()
# taxis = {'E': 10,
#          'K': 15,
#          'B': 30}
#
# for line in lines:
#     minutes, taxi, driver = line.split(' ')
#
#     if driver not in drivers:
#         drivers.append(driver)
#         salaries.append(int(minutes) * taxis[taxi])
#
#     elif driver in drivers:
#         num = drivers.index(driver)
#         salaries[num] += int(minutes) * taxis[taxi]
#
# print(drivers[salaries.index(max(salaries))])

# print(bin(1025)[2::].count('1'))
# print(int('a7', 16), int('251', 8))
# print(int('351', 8))
# print(int('125', 8))
# print(int('55', 16))
# print(int('75', 16))

# n = 0
# R = 0
#
# while R <= 75:
#     n += 1
#     N = n
#     n_third = ''
#     summ_third = 0
#
#     while N > 0:
#         n_third = str(N % 3) + n_third
#         summ_third += (N % 3)
#
#         N = N // 3
#
#     if summ_third % 2 == 0:
#         n_third.replace(n_third[0:2:], '2')
#         n_third = n_third + '0'
#     else:
#         n_third.replace(n_third[0:2:], '20')
#         n_third = n_third + '1'
#
#     R = int(n_third, 3)
#
# print(n)

data = open('9.csv').readlines()

# print(data[0])

lines = list()
lines_numbers = list()

for line in data:
    lines.append([int(number) for number in line.split(';')])

for g in range(len(lines)):
    line_ = lines[g]
    counters = list()

    for i in range(0, 8):
        counters.append(line_.count(line_[i]))

    three_times = line_[line_.index(3)]
    two_times = line_[line_.index(2)]

    if len(set(line_)) == 5 and counters.count(2) == 2 and counters.count(3) == 3:
        lines_numbers.append(g)

print(lines_numbers[2])
