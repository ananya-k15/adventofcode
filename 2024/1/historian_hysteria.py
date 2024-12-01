import math


with open("2024/1/input.txt") as text:

    pairs = 0
    left, right = {}, {}
    left_order = []
    for line in text:
        values = [int(i) for i in line.strip("\n").split("  ")]

        if values[0] not in left:
            left[values[0]] = 1
        else:
            left[values[0]] += 1
        left_order.append(values[0])

        if values[1] not in right:
            right[values[1]] = 1
        else:
            right[values[1]] += 1

        pairs += 1

    similarity = 0
    for val in left_order:
        if val in right:
            similarity += val * right[val]
    print("The similarity score is", similarity)

    diff = 0
    while pairs > 0:
        l = min(left.keys())
        r = min(right.keys())

        if left[l] == 1:
            left.pop(l)
        else:
            left[l] -= 1

        if right[r] == 1:
            right.pop(r)
        else:
            right[r] -= 1

        diff += abs(l - r)
        pairs -= 1

    print("The difference between the two lists is", diff)
