# calculate calibration value
def calibration_value(line):
    digits = [int(n) for n in line if n.isdigit()]
    value = digits[0] * 10 + digits[-1]
    return value


sum = 0
with open("day1/calibration_document.txt") as text:
    for line in text:
        sum += calibration_value(line)
print(sum)
