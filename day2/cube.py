import re

LIMIT = {"r": 12, "g": 13, "b": 14}
SUM = 0

game_num = 1
with open("day2/input.txt") as games:
    for game in games:
        # remove all whitespaces
        game = game.split(":")[1].replace(" ", "")
        # print(game)

        # split into sets
        sets = [s.split(",") for s in game.split(";")]

        flag = 0
        # check validity of each set
        for set in sets:
            for dice in set:
                num = re.match(r"[0-9]*", dice).group(0)
                # print(num, dice[len(num)])
                if int(num) > LIMIT[dice[len(num)]]:
                    flag = 1
                    break
            if flag:
                break
        else:
            SUM += game_num

        # update game number
        game_num += 1

print(SUM)
