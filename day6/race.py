import math

# get input
file = open("day6/input.txt").read().split("\n")
TIME = [int(x) for x in file[0][11:].split()]
DIST = [int(x) for x in file[1][11:].split()]

ftime = int(file[0][11:].replace(" ", ""))
fdist = int(file[1][11:].replace(" ", ""))

total = 1

# solve quadratic formula and get range
for i in range(0, len(TIME), 1):
    time = TIME[i]
    dist = DIST[i]

    x = math.sqrt(pow(time, 2) - 4 * dist)
    start = math.ceil(abs((x - time) / 2))
    end = math.floor(((x + time) / 2))

    # edge case
    if start * end == dist:
        start += 1
        end -= 1

    # print(start, end)

    # calculate number of ways to win for each input
    wins = end - start + 1
    total *= wins

# return total number of ways to win
print(total)

# part 2
x = math.sqrt(pow(ftime, 2) - 4 * fdist)
start = math.ceil(abs((x - ftime) / 2))
end = math.floor(((x + ftime) / 2))

# edge case
if start * end == dist:
    start += 1
    end -= 1

print(start, end)

# calculate number of ways to win for each input
wins = end - start + 1
print(wins)
