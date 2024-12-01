grid = []
x = 0
y = 0
steps = 0
line_len = 0

# get input into 2D array and find location of S
file = open("day10/example.txt").read().split("\n")
for line in file:
    row = [x for x in line]
    grid.append(["."] + row + ["."])
    if "S" in line:
        x = len(grid)
        y = line.index("S") + 1
        line_len = len(line) + 2
grid = [["." for x in range(line_len)]] + grid + [["." for x in range(line_len)]]


def print_grid():
    for i in grid:
        for j in i:
            print(j, end="")
        print()


print(x, y)
print_grid()

# start replacing characters with number of steps
def next(x, y, step):
    t = grid[x][y]
    grid[x][y] = step
    step += 1
    print_grid()
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    try:
        if type(grid[x + 1][y]) != int and grid[x + 1][y] in "|LJ":
            x1 = x + 1
            y1 = y
            temp = grid[x + 1][y]
            grid[x + 1][y] = step
            # if temp == "|":
            #     x += 2
            # elif temp == "L":
            #     x += 1
            #     y += 1
            # elif temp == "J":
            #     x += 1
            #     y -= 1
            # else:
            #     print("ERROR!!! at 1 ", x, y)
            # next(x, y, step + 1)
        if type(grid[x - 1][y]) != int and grid[x - 1][y] in "|F7":
            if x1 == 0 and y1 == 0:
                x1 = x - 1
                y1 = y
            else:
                x2 = x - 1
                y2 = y
            temp = grid[x - 1][y]
            grid[x - 1][y] = step
            # if temp == "|":
            #     x -= 2
            # elif temp == "F":
            #     x -= 1
            #     y += 1
            # elif temp == "7":
            #     x -= 1
            #     y -= 1
            # else:
            #     print("ERROR!!! at 2", x, y)
            # next(x, y, step + 1)
        if type(grid[x][y + 1]) != int and grid[x][y + 1] in "-J7":
            if x1 == 0 and y1 == 0:
                x1 = x
                y1 = y + 1
            else:
                x2 = x
                y2 = y + 1
            temp = grid[x][y + 1]
            grid[x][y + 1] = step
            # if temp == "-":
            #     y += 2
            # elif temp == "J":
            #     x -= 1
            #     y += 1
            # elif temp == "7":
            #     x += 1
            #     y += 1
            # else:
            #     print("ERROR!!! at 3 (", x, y, ") got value", temp)
            # next(x, y, step + 1)
        if type(grid[x][y - 1]) != int and grid[x][y - 1] in "-FL":
            temp = grid[x][y - 1]
            grid[x][y - 1] = step
            if x1 == 0 and y1 == 0:
                x1 = x
                y1 = y - 1
            else:
                x2 = x
                y2 = y - 1
            # if temp == "-":
            #     y -= 2
            # elif temp == "L":
            #     x -= 1
            #     y -= 1
            # elif temp == "F":
            #     x += 1
            #     y -= 1
            # else:
            #     print("ERROR!!! at 4", x, y)
            # next(x, y, step + 1)
        if x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0:
            step += 1
            next(x1, y1, step)
            next(x2, y2, step)
        else:
            print(x, y, t)
    except IndexError:
        print("index error")
    # if flag == False:
    #     print_grid()
    #     print("ERROR!!! at ", x, y)
    #     return


next(x, y, 0)
# return final number of steps
# if grid[x][y] == "|":
#     grid[x + 1][y] = steps
#     x += 1
# elif grid[x][y] == "L":
#     grid[x][y + 1] = steps
#     y += 1
# elif grid[x][y] == "J":
#     grid[x][y - 1] = steps
#     y -= 1
# continue
