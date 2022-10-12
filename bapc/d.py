import math
import random


def jump(count, points, print_maxes):
    maxes = [[-math.inf for _ in range(count)] for _ in range(count)]

    for step in range(count):
        for spot in range(count - 1, -1, -1):
            if step + spot < count - 1:
                if step + spot == count - 2:
                    maxes[spot][step] = points[count - 1]
                elif step == 0:
                    maxes[spot][0] = maxes[spot + 1][0] + points[spot + 1]
                elif step > 1 and spot > 0:
                    maxes[spot][step] = maxes[spot + 1][step - 1]
                else:
                    target_spot = spot + step + 1
                    max_from_spot = max(maxes[target_spot][:step + 1])
                    maxes[spot][step] = max_from_spot + points[target_spot]

    if print_maxes:
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        print("\t".join(map(str, range(len(maxes) + 1))))
        for index, row in enumerate(maxes):
            print("\t".join(map(str, [alphabet[index]] + row)))

    return max(maxes[0]) + points[0]


if __name__ == "__main__":
    USE_INPUT = True
    RANDOM_COUNT = 3000
    RANDOM_RANGE = 1_000_000_000
    COUNT = int(input()) if USE_INPUT else RANDOM_COUNT
    POINTS = [int(x) for x in input().split(" ")] if USE_INPUT else random.sample(
        range(-RANDOM_RANGE, RANDOM_RANGE + 1), COUNT)
    print(jump(COUNT, POINTS, False))
