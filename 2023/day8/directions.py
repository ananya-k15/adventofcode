from math import gcd

# get input
file = open("day8/input.txt").read().split("\n")
STEPS = []
START = []

# create dictionary and list of instructions
lr = {"L": 0, "R": 1}
instructions = [lr[x] for x in file[0]]
reference = {}
for line in file[2:]:
    reference[line[0:3]] = (line[7:10], line[12:15])
    if "A" in line[0:3]:
        START.append(line[0:3])

# loop to repeat instructions until ZZZ
for state in START:
    steps = 0
    while "Z" not in state:
        for i in instructions:
            temp = reference[state][i]
            state = temp
        steps += len(instructions)
    STEPS.append(steps)

# return number of steps
print(STEPS)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# calculate LCM
LCM = 1
for num in STEPS:
    LCM = lcm(LCM, num)
print(LCM)
