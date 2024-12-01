SUM = 0
SEQUENCES = []
NEXT_BACK = []
NEXT_FORWARD = []

# get list of sequences
file = open("day9/input.txt").read().split("\n")
for line in file:
    lis = [int(x) for x in line.split()]
    SEQUENCES.append(lis)

# add the next number in sequence
def next_back(lis):
    new = [lis[i + 1] - lis[i] for i in range(0, len(lis) - 1)]
    if new.count(0) == len(new):
        new.append(0)
        final = lis + [new[-1] + lis[-1]]
    else:
        diff = next_back(new)
        final = lis + [diff[-1] + lis[-1]]
    return final


# add the first number in sequence
def next_forward(lis):
    new = [lis[i + 1] - lis[i] for i in range(0, len(lis) - 1)]
    if new.count(0) == len(new):
        new.append(0)
        final = [lis[0] - new[0]] + lis
    else:
        diff = next_forward(new)
        final = [lis[0] - diff[0]] + lis
    return final


# calculate next number in each sequence
for seq in SEQUENCES:
    # NEXT_BACK.append(next_back(seq)[-1])
    NEXT_FORWARD.append(next_forward(seq)[0])

# return sum
# print(sum(NEXT_BACK))
print(sum(NEXT_FORWARD))
