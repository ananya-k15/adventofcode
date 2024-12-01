import regex as re

CONVERT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# calculate calibration value
def calibration_value(line):
    digits = re.findall(
        r"[1-9]|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True
    )
    # print(digits)
    value = 0
    value += int(digits[0]) if digits[0].isdigit() else CONVERT[digits[0]]
    value *= 10
    value += int(digits[-1]) if digits[-1].isdigit() else CONVERT[digits[-1]]
    return value


sum = 0
with open("day1/calibration_document.txt") as text:
    for line in text:
        sum += calibration_value(line)
print(sum)
