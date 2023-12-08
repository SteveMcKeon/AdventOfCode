# Function to find the minimum number of cubes needed for each color
def find_min_cubes(game_data):
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for group in game_data.split(';'):
        current_cubes = {'red': 0, 'green': 0, 'blue': 0}
        cubes = group.split(',')
        for cube in cubes:
            count, color = cube.strip().split(' ')
            current_cubes[color] += int(count)
        for color in min_cubes:
            min_cubes[color] = max(min_cubes[color], current_cubes[color])
    return min_cubes

# Function to calculate the power of a set of cubes
def calculate_power(cubes):
    return cubes['red'] * cubes['green'] * cubes['blue']

# Read games from file and calculate the power of minimum sets
total_power = 0
with open('input.txt', 'r') as file:
    for line in file:
        _, game_data = line.split(':', 1)
        min_cubes = find_min_cubes(game_data.strip())
        total_power += calculate_power(min_cubes)

print(total_power)
