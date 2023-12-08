# VERY SLOW, I just left it overnight to run
#  A better solution: I figure you could do something like, load first seed, then at each list, look ahead to see how far away the next change in sequence would be.
#  One of those lists will have the smallest gap, so next seed try [original seed + determined gap].

def process_mapping(lines):
    mapping = []
    for line in lines:
        dest_start, src_start, length = map(int, line.split())
        mapping.append((src_start, dest_start, length))
    return mapping


def find_mapped_value(value, mapping):
    for src_start, dest_start, length in mapping:
        if src_start <= value < src_start + length:
            return dest_start + (value - src_start)
    return value


file_path = 'input.txt'

# Reading and processing the file
with open(file_path, 'r') as file:
    content = file.read().splitlines()

# Extracting initial seeds
seeds = list(map(int, content[0].split(': ')[1].split()))

# Parsing the mappings
seed_to_soil = process_mapping(content[4:16])
soil_to_fertilizer = process_mapping(content[19:39])
fertilizer_to_water = process_mapping(content[42:89])
water_to_light = process_mapping(content[92:130])
light_to_temperature = process_mapping(content[133:148])
temperature_to_humidity = process_mapping(content[151:157])
humidity_to_location = process_mapping(content[160:190])


# Function to get the final location for a seed
def get_final_location(seed):
    soil = find_mapped_value(seed, seed_to_soil)
    fertilizer = find_mapped_value(soil, soil_to_fertilizer)
    water = find_mapped_value(fertilizer, fertilizer_to_water)
    light = find_mapped_value(water, water_to_light)
    temperature = find_mapped_value(light, light_to_temperature)
    humidity = find_mapped_value(temperature, temperature_to_humidity)
    location = find_mapped_value(humidity, humidity_to_location)
    return location


# Finding the lowest location number considering the seed and the count
lowest_location = float('inf')
for i in range(0, len(seeds), 2):
    seed = seeds[i]
    count = seeds[i + 1]
    for j in range(count):
        location = get_final_location(seed + j)
        lowest_location = min(lowest_location, location)

print(lowest_location)
