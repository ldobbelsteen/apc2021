# MF 6, team 404namenotfound

import math
import time

# n = 100000
# k = 100000
# temps = [0] * n
# for i in range(n):
#     temps[i] = random.randint(0, 2000002) - 1000000
# thick = [0] * k
# for i in range(k):
#     thick[i] = random.randint(1, 1000001)

nk = input().split(" ")
n = int(nk[0])
k = int(nk[1])
temps = [int(x) for x in input().split(" ")]
thicks = [int(x) for x in input().split(" ")]

icethick, scating = [0] * n, [0] * k
icethick[0] = (min(0, (temps[0] / 5.0))) * (-1)
for i in range(1, n):
    icethick[i] = min(0, (temps[i] / 5.0) + icethick[i - 1]) * (-1)

icethick.sort(reverse=True)

dayThick = []
for thick in icethick:
    thick = math.floor(thick)
    if len(dayThick) > 0:
        if dayThick[-1][0] == thick:
            dayThick[-1] = (thick, dayThick[-1][1] + 1)
        else:
            dayThick.append((thick, dayThick[-1][1] + 1))
    else:
        dayThick.append((thick, 1))

for i in range(len(thicks)):
    k = thicks[i]
    sett = False
    a = 0
    for j in range(len(dayThick)):
        if k > dayThick[j][0]:
            a = j
            sett = True
            break
    if sett:
        scating[i] = dayThick[min(a - 1, 0)][1]
    else:
        scating[i] = 0

    # print(time.time())
print(" ".join([str(x) for x in scating]))
# print(min(0,  (-3 / 5.0))
