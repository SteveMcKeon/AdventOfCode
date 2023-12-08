# Function to check if a game is possible
def is_game_possible(game_data, max_cubes):
    for group in game_data.split(';'):
        cubes = group.split(',')
        for cube in cubes:
            count, color = cube.strip().split(' ')
            if int(count) > max_cubes[color]:
                return False
    return True


# Maximum number of cubes in the bag
max_cubes = {'red': 12, 'green': 13, 'blue': 14}

# Read games from file and check if they are possible
possible_games_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        game_id, game_data = line.split(':', 1)
        game_id = int(game_id.split()[1])  # Extract game ID
        if is_game_possible(game_data.strip(), max_cubes):
            possible_games_sum += game_id

print(possible_games_sum)
