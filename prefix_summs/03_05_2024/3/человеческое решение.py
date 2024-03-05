from itertools import combinations as combinations


with open("3/28130_B.txt") as f:
    nums = map(int, f.readlines()[1:])

print(len(list(
    filter(lambda x: x % 80 == 0,
        map(lambda x: x[0] + x[1],
            filter(lambda x: x[0] > 50 or x[1] > 50, combinations(nums, 2))
        )
    )
)))