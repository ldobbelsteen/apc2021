import math

data = input().split(" ")
n = int(data[0])
t = int(data[1])

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

subalpha = alphabet[:n]
r_subalpha = subalpha[:]
r_subalpha.reverse()

i = math.floor(t / (n * n))
j = math.floor((t - i * n * n) / n)
k = t - i * n * n - j * n

bruh = []
bruh += r_subalpha * i
bruh += r_subalpha[:j]
if k > 0:
    bruh += subalpha[k-j-1]

print(len(bruh))
print(" ".join(bruh))

# order = ""
# count = 0
# items = alphabet[:n]
# leftover = t
# while leftover > 0:
#     idx = min(leftover - 1, n - 1)
#     if leftover - (idx + 1) == 1:
#         idx -= 1
#     item = items.pop(idx)
#     count += 1
#     order += item + " "
#     items.insert(0, item)
#     leftover -= idx + 1

# print(count)
# print(order[:-1])
