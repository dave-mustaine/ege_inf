from ipaddress import *

# count = 0  # https://education.yandex.ru/ege/task/8d934235-8255-4347-b429-abc655c58790
#
# for ip in ip_network('136.36.240.16/255.255.255.248'):
#     if bin(int(ip))[2:].count('101') == 0:
#         count += 1
#
# print(count)

# count = 0  # https://education.yandex.ru/ege/task/4ed15fe1-a07d-45b1-ae66-6759f78b8c25
#
# for ip in ip_network('49.26.38.128/255.255.255.192').hosts():
#     if int(bin(int(ip))[-8:], 2) % 2 != 0:
#         count += 1
#
# print(count)

count = 0  # https://education.yandex.ru/ege/task/8279c0b0-e9f8-475e-b863-e94d12a87048

for ip in ip_network('114.179.203.128/255.255.255.192').hosts():
    if bin(int(ip))[2:].count('1') % 3 == 0:
        count += 1

print(count)
