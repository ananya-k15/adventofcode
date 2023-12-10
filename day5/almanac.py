# read file
file = open("day5/input.txt").read().split("\n")
SEEDS = [int(x) for x in file[0][7:].split()]
LOCATIONS = []

# function to build each dictionary
def build_dict(start, end, name):
    ranges = file[start:end]
    for i in ranges:
        values = i.split()
        val1 = int(values[0])
        val2 = int(values[1])
        end = int(values[2])

        while end > 0:
            name[val2] = val1
            val1 += 1
            val2 += 1
            end -= 1
    print("built.")


# all dicts to be build
SEED_TO_SOIL = {}
SOIL_TO_FERTILIZER = {}
FERTILIZER_TO_WATER = {}
WATER_TO_LIGHT = {}
LIGHT_TO_TEMP = {}
TEMP_TO_HUMIDITY = {}
HUMIDITY_TO_LOCATION = {}

# build dicts
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
        build_dict(start, end, FERTILIZER_TO_WATER)
        start = ind + 1
    elif file[ind] == "water-to-light map:":
        end = ind - 1
        build_dict(start, end, WATER_TO_LIGHT)
        start = ind + 1
    elif file[ind] == "light-to-temperature map:":
        end = ind - 1
        build_dict(start, end, LIGHT_TO_TEMP)
        start = ind + 1
    elif file[ind] == "temperature-to-humidity map:":
        end = ind - 1
        build_dict(start, end, TEMP_TO_HUMIDITY)
        start = ind + 1
    elif file[ind] == "humidity-to-location map:":
        end = ind - 1
        build_dict(start, end, HUMIDITY_TO_LOCATION)
        start = ind + 1
    else:
        continue

# check
print("done")
# for k, v in SEED_TO_SOIL.items():
#     print(k, " : ", v)

# map each seed to a location number
for seed in SEEDS:
    soil = SEED_TO_SOIL.get(seed, seed)
    fertilizer = SOIL_TO_FERTILIZER.get(soil, soil)
    water = FERTILIZER_TO_WATER.get(fertilizer, fertilizer)
    light = WATER_TO_LIGHT.get(water, water)
    temp = LIGHT_TO_TEMP.get(light, light)
    humidity = TEMP_TO_HUMIDITY.get(temp, temp)
    location = HUMIDITY_TO_LOCATION.get(humidity, humidity)

    # print(seed, soil, fertilizer, water, light, temp, humidity, location)

    LOCATIONS.append(location)


# find lowest location and coresponding seed number
loc = min(LOCATIONS)
print(loc)
