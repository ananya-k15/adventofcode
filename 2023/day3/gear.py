import time
import re

start = time.time()
SUM = 0

text = open("day3/input.txt").read()
schematic = text.split("\n")
line_num = 0
line_len = len(schematic[0])
last = []

while line_num < len(schematic):
    parts = re.finditer(r"[0-9]+", schematic[line_num])
    for match in parts:
        if match != None:
            a = match.start()
            b = match.end()
            number = int(schematic[line_num][a:b])

            search = ""

            if line_num != 0 and line_num != len(schematic) - 1:
                if a > 0 and b < line_len:
                    search = (
                        schematic[line_num - 1][a - 1 : b + 1]
                        + schematic[line_num][a - 1]
                        + schematic[line_num][b]
                        + schematic[line_num + 1][a - 1 : b + 1]
                    )
                elif a > 0:
                    search = (
                        schematic[line_num - 1][a - 1 : b]
                        + schematic[line_num][a - 1]
                        + schematic[line_num + 1][a - 1 : b]
                    )
                elif b < line_len:
                    search = (
                        schematic[line_num - 1][a : b + 1]
                        + schematic[line_num][b]
                        + schematic[line_num + 1][a : b + 1]
                    )
            elif line_num == 0:
                if a > 0 and b < line_len:
                    search = (
                        schematic[line_num][a - 1]
                        + schematic[line_num][b]
                        + schematic[line_num + 1][a - 1 : b + 1]
                    )
                elif a > 0:
                    search = (
                        schematic[line_num][a - 1] + schematic[line_num + 1][a - 1 : b]
                    )
                elif b < line_len:
                    search = schematic[line_num][b] + schematic[line_num + 1][a : b + 1]
            elif line_num == len(schematic) - 1:
                if a > 0 and b < line_len:
                    search = (
                        schematic[line_num - 1][a - 1 : b + 1]
                        + schematic[line_num][a - 1]
                        + schematic[line_num][b]
                    )
                elif a > 0:
                    search = (
                        schematic[line_num - 1][a - 1 : b] + schematic[line_num][a - 1]
                    )
                elif b < line_len:
                    search = schematic[line_num - 1][a : b + 1] + schematic[line_num][b]

            # check if search has any special characters
            match = re.search(r"[^0-9\.]", search)
            if match != None:
                SUM += number
    line_num += 1

print(SUM)
