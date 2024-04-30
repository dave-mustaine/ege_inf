# max_substring = 0
#
# with open("24.txt", "r") as f:
#     text = f.readlines()[0]
#
# for left in range(0, len(text)):
#     for right in range(left + 1, len(text)):
#         if text[left] == text[right]:
#             break
#     max_substring = max((right - left + 1), max_substring)
#
# print(max_substring)

max_substring = 0

with open("24.txt", "r") as f:
    text = f.readlines()[0]

for left in range(0, len(text)):
    for right in range(left + 1, len(text)):
        if text[left] == text[right]:
            break
    max_substring = max((right - left + 1), max_substring)

print(max_substring)
