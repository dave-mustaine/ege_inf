# print('w x y z F')
#
# for w in (0, 1):
#     for x in (0, 1):
#         for y in (0, 1):
#             for z in (0, 1):
#                 f = (w == z) or (x and (not y)) or w
#
#                 if not f:
#                     print(w, x, y, z, f)

a = '1' + '0' * 60

while '1' in a:
    if '10' in a:
        a = a.replace('10', '0001')
    else:
        a = a.replace('1', '00')

print(len(a))
