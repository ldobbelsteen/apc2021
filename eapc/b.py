n = int(input())
distances = [int(x) for x in input().split(" ")]

distances.sort(reverse=True)

dist = 2 * distances[0]
for i in range(1, len(distances) - 1):
    dist += distances[i]

print(dist)
