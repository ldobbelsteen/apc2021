import math

data = input().split(" ")
number_of_countries = int(data[0])
number_of_borders = int(data[1])

data = input().split(" ")
starting_country = int(data[0])
target_country = int(data[1])
start_candy_count = int(data[2])

neighbours = {}
max_candy_count = {}
for i in range(1, number_of_countries + 1):
    max_candy_count[i] = 0
    neighbours[i] = []
max_candy_count[starting_country] = start_candy_count

for _ in range(number_of_borders):
    data = input().split(" ")
    first = int(data[0])
    second = int(data[1])
    leftover_after_tax = 1 - (float(data[2]) / 100)
    neighbours[first].append((second, leftover_after_tax))
    neighbours[second].append((first, leftover_after_tax))

queue = list(range(1, number_of_countries + 1))
while len(queue) > 0:
    queue.sort(key=max_candy_count.get)
    country = queue.pop()
    for neighbour in neighbours[country]:
        sug_candies = math.floor(max_candy_count[country] * neighbour[1])
        if sug_candies > max_candy_count[neighbour[0]]:
            max_candy_count[neighbour[0]] = sug_candies

print(max_candy_count[target_country])
