import time
import re

start = time.time()


text = open("day3/input.txt").read()
schematic = text.split("\n")
line_num = 0
line_len = len(schematic[0])
last = []
grid = []


def build_grid():
    for line in schematic:
        row = []
        for ch in line:
            if ch == "*":
                row.append([])
            else:
                row.append(None)
        grid.append(row)


def print_grid():
    for x in grid:
        for y in x:
            print(y, end="")
        print()


def return_sum():
    total = 0
    for x in grid:
        for y in x:
            if y != None and len(y) == 2:
                print(y)
                gear_ratio = y[0] * y[1]
                total += gear_ratio
    return total


def print_schematic():
    for i in schematic[:2]:
        print(i)


def print_list():
    for i in last:
        print(i, end=", ")
    print()


build_grid()

while line_num < len(schematic):
    parts = re.finditer(r"[0-9]+", schematic[line_num])
    for match in parts:
        if match != None:
            a = match.start()
            b = match.end()
            number = int(schematic[line_num][a:b])

            # print(number)

            search = []

            if line_num != 0 and line_num != len(schematic) - 1:
                if a > 0 and b < line_len:
                    search.append(schematic[line_num - 1][a - 1 : b + 1])
                    search.append(schematic[line_num][a - 1] + schematic[line_num][b])
                    search.append(schematic[line_num + 1][a - 1 : b + 1])
                elif a > 0:
                    search.append(schematic[line_num - 1][a - 1 : b])
                    search.append(schematic[line_num][a - 1])
                    search.append(schematic[line_num + 1][a - 1 : b])
                elif b < line_len:
                    search.append(schematic[line_num - 1][a : b + 1])
                    search.append(schematic[line_num][b])
                    search.append(schematic[line_num + 1][a : b + 1])
            elif line_num == 0:
                if a > 0 and b < line_len:
                    search.append(None)
                    search.append(schematic[line_num][a - 1] + schematic[line_num][b])
                    search.append(schematic[line_num + 1][a - 1 : b + 1])
                elif a > 0:
                    search.append(None)
                    search.append(schematic[line_num][a - 1])
                    search.append(schematic[line_num + 1][a - 1 : b])
                elif b < line_len:
                    search.append(None)
                    search.append(schematic[line_num][b])
                    search.append(schematic[line_num + 1][a : b + 1])
            elif line_num == len(schematic) - 1:
                if a > 0 and b < line_len:
                    search.append(schematic[line_num - 1][a - 1 : b + 1])
                    search.append(schematic[line_num][a - 1] + schematic[line_num][b])
                    search.append(None)
                elif a > 0:
                    search.append(schematic[line_num - 1][a - 1 : b])
                    search.append(schematic[line_num][a - 1])
                    search.append(None)
                elif b < line_len:
                    search.append(schematic[line_num - 1][a : b + 1])
                    search.append(schematic[line_num][b])
                    search.append(None)

            # check if search has any special characters
            for i in range(-1, 2, 1):
                if search[i + 1] != None:
                    matchlist = re.finditer(r"\*", search[i + 1])
                    for match in matchlist:
                        if match != None:
                            x = line_num + i
                            if i == 0:
                                if match.start() == 0:
                                    y = a - 1
                                else:
                                    y = a + len(str(number))
                                # y = (
                                #     a
                                #     - len(str(number))
                                #     + match.start()
                                #     - len(search[i + 1])
                                #     + 1
                                # )
                            else:
                                if a == 0:
                                    y = a + match.start()
                                else:
                                    y = a - 1 + match.start()

                                # y = (
                                #     a
                                #     + len(str(number))
                                #     + match.start()
                                #     - len(search[i + 1])
                                #     + 1
                                # )
                            print(x, y, number)
                            print(type(grid[x][y]))
                            grid[x][y].append(number)
    line_num += 1


SUM = return_sum()
print(SUM)
