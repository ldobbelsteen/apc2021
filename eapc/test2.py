n = input()
n = int(n)
r = input()
r = r.split(" ")
r = [int(x) for x in r]

hoo = list(range(1, n+1))
for number in r:

    hoo.remove(number)

print(hoo[0])
