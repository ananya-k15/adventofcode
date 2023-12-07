import re

SUM = 0

with open("day2/input.txt") as games:
    for game in games:
        # create new dictionary with new powers
        MAX = {"r": 0, "b": 0, "g": 0}

        # remove all whitespaces
        game = game.split(":")[1].replace(" ", "")
        # print(game)

        # split into sets
        sets = [s.split(",") for s in game.split(";")]

        power = 1
        # calculate power of each set
        for set in sets:
            for dice in set:
                num = re.match(r"[0-9]*", dice).group(0)
                # print(num, dice[len(num)])
                if int(num) > MAX[dice[len(num)]]:
                    MAX[dice[len(num)]] = int(num)
        else:
            power = MAX["r"] * MAX["b"] * MAX["g"]
            SUM += power

print(SUM)
