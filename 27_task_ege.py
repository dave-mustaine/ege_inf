# # 27-1 (server -> Задания -> ЕГЭ2024)
# file_1 = open('27-A1.txt').readlines()
# file_2 = open('27-B1.txt').readlines()
#
# n1 = int(file_2[0])
# data = []
#
# for text in file_2[1:]:
#     data.append(sorted([int(i) for i in text.split()]))
#
# s = 0
# min_d = 0
#
# for i in data:
#     s += i[0]
#     if i[1] - i[0] % 10:
#         min_d = min(i[1] - i[0], min_d)
#
# print(s)

# # 27-2 (server -> Задания -> ЕГЭ2024)
# file_1 = open('27-1a.txt').readlines()
# file_2 = open('27-1b.txt').readlines()
#
# m_21 = 0
# m_7 = 0
# m_3 = 0
# m_not = 0
#
# # n = int(file_2[0])
# data = []
#
# for text in file_1[1:]:
#     data.append(int(text))
#
# for i in data:
#     if i % 21 == 0 and i >= m_21:
#         m_21 = i
#     elif i % 7 == 0 and i >= m_7:
#         m_7 = i
#     elif i % 3 == 0 and i >= m_3:
#         m_3 = i
#     elif i > m_not:
#         m_not = i
#
# print(max(m_7 * m_3, m_21 * m_not, m_21 * m_3, m_21 * m_7))
# print(m_21, m_7, m_3, m_not)

# 27-3 (server -> Задания -> ЕГЭ2024)
file_1 = open('27-A.txt').readlines()
file_2 = open('27-B.txt').readlines()
