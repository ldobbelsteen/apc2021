# MF 6 404 name not found

import math

nk = input().split(" ")
n = int(nk[0])
s = int(nk[1])
k = int(nk[2])
points = [int(x) for x in input().split(" ")]
lijst = [0] * n
for item in points:
    lijst[math.ceil(item / s) - 1] += 1

top = max(lijst)
for i in range(top, 0, -1):
    temp = ""
    for item in lijst:
        temp = temp + "." if item < i else temp + "#"
    print(temp)
print("-" * n)
