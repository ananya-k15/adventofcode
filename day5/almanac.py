# read file
file = open("day5/example.txt").read().split("\n")
FULL = [int(x) for x in file[0][7:].split()]
SEEDS = [[FULL[i], FULL[i + 1]] for i in range(0, len(FULL), 2)]
RANGE = []
LOCATIONS = []
# print(SEEDS)

# function to build each dictionary
def build_dict(start, end, name):
    ranges = file[start:end]
    for i in ranges:
        values = [int(x) for x in i.split()]
        name.append(values)
    # print(name)


# all dicts to be build
SEED_TO_SOIL = []
SOIL_TO_FERTILIZER = []
FERTILIZER_TO_WATER = []
WATER_TO_LIGHT = []
LIGHT_TO_TEMP = []
TEMP_TO_HUMIDITY = []
HUMIDITY_TO_LOCATION = []

# build lists
num_lines = len(file)
start = 0
end = 0
for ind in range(1, num_lines, 1):
    if file[ind] == "":
        continue
    elif file[ind] == "seed-to-soil map:":
        start = ind + 1
    elif file[ind] == "soil-to-fertilizer map:":
        end = ind - 1
        build_dict(start, end, SEED_TO_SOIL)
        start = ind + 1
    elif file[ind] == "fertilizer-to-water map:":
        end = ind - 1
        build_dict(start, end, SOIL_TO_FERTILIZER)
        start = ind + 1
    elif file[ind] == "water-to-light map:":
        end = ind - 1
        build_dict(start, end, FERTILIZER_TO_WATER)
        start = ind + 1
    elif file[ind] == "light-to-temperature map:":
        end = ind - 1
        build_dict(start, end, WATER_TO_LIGHT)
        start = ind + 1
    elif file[ind] == "temperature-to-humidity map:":
        end = ind - 1
        build_dict(start, end, LIGHT_TO_TEMP)
        start = ind + 1
    elif file[ind] == "humidity-to-location map:":
        end = ind - 1
        build_dict(start, end, TEMP_TO_HUMIDITY)
        start = ind + 1
    else:
        continue
else:
    end = ind
    build_dict(start, end, HUMIDITY_TO_LOCATION)

# check
print("done")

# find corresponding value
def find_in_dict(lis, value, range):
    # print(value)
    for i in lis:
        diff = value - i[1]
        if value in range(i[1], i[1] + i[2]):
            return i[0] + value - i[1]
    return value


# map each seed to a location number
for s in SEEDS:
    for seed in range(s[0], s[0] + s[1], 1):
        print(seed)
        soil = find_in_dict(SEED_TO_SOIL, seed)
        fertilizer = find_in_dict(SOIL_TO_FERTILIZER, soil)
        water = find_in_dict(FERTILIZER_TO_WATER, fertilizer)
        light = find_in_dict(WATER_TO_LIGHT, water)
        temp = find_in_dict(LIGHT_TO_TEMP, light)
        humidity = find_in_dict(TEMP_TO_HUMIDITY, temp)
        location = find_in_dict(HUMIDITY_TO_LOCATION, humidity)

        # print(seed, soil, fertilizer, water, light, temp, humidity, location)

        LOCATIONS.append(location)


# find lowest location and coresponding seed number
loc = min(LOCATIONS)
# print(LOCATIONS)
print(loc)
