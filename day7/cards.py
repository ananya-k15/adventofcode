from functools import cmp_to_key

# read input
file = open("day7/input.txt").read().split("\n")

# assign variables
importance = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
}
FIVE = []
FOUR = []
FULL = []
THREE = []
TWO = []
ONE = []
HIGH = []
TOTAL = 0

# divide into lists
for i in file:
    hand = i[0:5]
    bid = int(i[6:])

    value = max(set(hand), key=hand.count)
    freq = hand.count(value)

    if freq == 5:
        FIVE.append([hand, bid])
    elif freq == 4:
        FOUR.append([hand, bid])
    elif freq == 3:
        dupe = hand.replace(value, "")
        if dupe[0] == dupe[1]:
            FULL.append([hand, bid])
        else:
            THREE.append([hand, bid])
    elif freq == 2:
        dupe = hand.replace(value, "")
        value2 = max(set(dupe), key=dupe.count)
        freq2 = dupe.count(value2)
        if freq2 == 2:
            TWO.append([hand, bid])
        elif freq2 == 1:
            ONE.append([hand, bid])
    elif freq == 1:
        HIGH.append([hand, bid])
        # print(hand, "goes to HIGH")


def compare(v1, v2):
    for i in range(0, 5, 1):
        diff = importance[v1[0][i]] - importance[v2[0][i]]
        if diff == 0:
            continue
        else:
            return int(diff / abs(diff))


# print(HIGH)
# print(ONE)
# print(TWO)
# print(THREE)
# print(FULL)
# print(FOUR)
# print(FIVE)

# make final list and calculate bids
FIVE.sort(key=cmp_to_key(compare), reverse=True)
FOUR.sort(key=cmp_to_key(compare), reverse=True)
FULL.sort(key=cmp_to_key(compare), reverse=True)
THREE.sort(key=cmp_to_key(compare), reverse=True)
TWO.sort(key=cmp_to_key(compare), reverse=True)
ONE.sort(key=cmp_to_key(compare), reverse=True)
HIGH.sort(key=cmp_to_key(compare), reverse=True)

FINAL = HIGH + ONE + TWO + THREE + FULL + FOUR + FIVE
# print(FINAL)
for p in range(0, len(FINAL), 1):
    bet = FINAL[p][1] * (p + 1)
    TOTAL += bet

print(TOTAL)
