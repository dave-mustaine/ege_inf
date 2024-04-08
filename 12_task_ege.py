# n = '1666'
# num_of_three = 0
#
# while num_of_three <= 5:
#     a = n
#     while '66' in a or '111' in a:
#         while '6666' in a:
#             if '6666' in a:
#                 a = a.replace('6666', '1')
#             else:
#                 a = a.replace('111', '3')
#
#         if '66' in a:
#             a = a.replace('66', '6')
#
#     num_of_three = a.count('3')
#
#     print(a, num_of_three)
#
#     n = n + '6'

a = '5' * 200
while '555' in a or '333' in a:
    if '555' in a:
        a = a.replace('555', '3')
    else:
        a = a.replace('333', '5')

numm = 0

for i in range(len(a)):
    numm += int(a[i])

print(numm)
