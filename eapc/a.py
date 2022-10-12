import math

n = int(input())
r = [int(x) for x in input().split(" ")]
r_copy = r[:]
r_copy.sort()
for i in range(0, math.floor(0.5 * n)):
    for j in range(n - 1, math.floor(0.5 * n) - 1, -1):
        if r_copy[j] % r_copy[i] == 0:
            r_i_index = r.index(r_copy[i])
            r_j_index = r.index(r_copy[j])
            print(r_i_index + 1, r_j_index + 1)
            exit()
