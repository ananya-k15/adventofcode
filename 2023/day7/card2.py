from functools import cmp_to_key

# read input
file = open("day7/input.txt").read().split("\n")

# assign variables
importance = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "T": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12,
    "J": 13,
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
    if value == "J" and freq != 5:
        val2 = max(set(hand.replace("J", "")), key=hand.count)
        value = val2
        dupe1 = hand.replace("J", val2)
        freq += hand.count(val2)
    elif value != "J":
        freq += hand.count("J")
        dupe1 = hand.replace("J", value)
    else:
        dupe1 = hand

    if freq == 5:
        FIVE.append([hand, bid])
    elif freq == 4:
        FOUR.append([hand, bid])
    elif freq == 3:
        dupe2 = dupe1.replace(value, "")
        # print(hand, dupe1)
        if dupe2[0] == dupe2[1]:
            FULL.append([hand, bid])
        else:
            THREE.append([hand, bid])
    elif freq == 2:
        dupe2 = dupe1.replace(value, "")
        value2 = max(set(dupe2), key=dupe2.count)
        freq2 = dupe2.count(value2)
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


# make final list and calculate bids
FIVE.sort(key=cmp_to_key(compare), reverse=True)
FOUR.sort(key=cmp_to_key(compare), reverse=True)
FULL.sort(key=cmp_to_key(compare), reverse=True)
THREE.sort(key=cmp_to_key(compare), reverse=True)
TWO.sort(key=cmp_to_key(compare), reverse=True)
ONE.sort(key=cmp_to_key(compare), reverse=True)
HIGH.sort(key=cmp_to_key(compare), reverse=True)

# print(HIGH)
# print(ONE)
# print(TWO)
# print(THREE)
# print(FULL)
# print(FOUR)
# print(FIVE)

FINAL = HIGH + ONE + TWO + THREE + FULL + FOUR + FIVE
# print(FINAL)
for p in range(0, len(FINAL), 1):
    bet = FINAL[p][1] * (p + 1)
    TOTAL += bet

print(TOTAL)
