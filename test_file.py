n = 0
r = 0

while r < 76:
    n += 1
    bin_n = bin(n)[2::]

    if (n % 3) == 0:
        bin_n = bin_n + bin_n[-3::]
    else:
        bin_n = bin_n + bin((n % 3) * 3)[2::]

    r = int(bin_n, 2)

    print(n, r)
