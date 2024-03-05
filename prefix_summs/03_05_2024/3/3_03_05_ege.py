with open('28130_A.txt') as f:
    text = list(map(int, f.readlines()))

s = [0] * 80
s_50 = [0] * 80

pairs = 0

for i in text:
    if i <= 50:
        s[i % 80] += 1
    else:
        s_50[i % 80] += 1

for i in range(len(s) - 1):
    pairs += (s[i + 1] * s_50[-(i + 1)]) / 2
