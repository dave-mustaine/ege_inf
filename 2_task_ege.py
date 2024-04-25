# print('w x y z F')
#
# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             for w in (0, 1):
#                 f = ((not x) and ((not ((not z) or y)) or w))
#
#                 if not f:
#                     print(w, x, y, z, f)

print('w x y z F')

for w in (0, 1):
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                f = (y and (x or z)) or (not (y or z)) or w

                if not f:
                    print(w, x, y, z, f)
