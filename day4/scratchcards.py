total = 0
copies = [1 for i in range(0, 209, 1)]
# copies = [1 for i in range(0, 7, 1)]
cardno = 1

with open("day4/input.txt") as file:
    for line in file:
        winning_nums = [int(x) for x in line[10:39].split()]
        # winning_nums = [int(x) for x in line[8:22].split()]
        wins = -1
        nums = [int(x) for x in line[42:].split()]
        # nums = [int(x) for x in line[25:].split()]
        for i in nums:
            if i in winning_nums:
                wins += 1
        # print("WINS : ", wins)
        if wins >= 0:
            total += pow(2, wins)
        wins += 1
        # print(cardno, wins)
        while wins > 0:
            # print(cardno, wins)
            if cardno + wins < len(copies):
                copies[cardno + wins] += copies[cardno]
            wins -= 1
        # print(cardno, copies)
        cardno += 1

print(sum(copies) - 1)
print(total)
