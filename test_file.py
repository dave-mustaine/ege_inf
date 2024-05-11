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

lines = '''25 K Igor
11 E Kirill
15 B Anna
20 E Igor
7 E Anna
13 E Kirill
21 E Anna
33 K Ivan
17 E Kirill
20 E Anna'''.split('\n')

drivers = list()
salaries = list()
taxis = {'E': 10,
         'K': 15,
         'B': 30}

for line in lines:
    minutes, taxi, driver = line.split(' ')

    if driver not in drivers:
        drivers.append(driver)
        salaries.append(int(minutes) * taxis[taxi])

    elif driver in drivers:
        num = drivers.index(driver)
        salaries[num] += int(minutes) * taxis[taxi]

print(drivers[salaries.index(max(salaries))])
