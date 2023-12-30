def parse_input(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid


def find_start_position(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                return x, y
    return None


def find_loop_len(start, curr_dir, grid):
    directions = {
        'N': (0, -1),
        'S': (0, 1),
        'E': (1, 0),
        'W': (-1, 0),
    }
    opposite_dir = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E',
    }
    pipes = {
        '|': ('N', 'S'),
        '-': ('E', 'W'),
        'L': ('N', 'E'),
        'J': ('N', 'W'),
        '7': ('S', 'W'),
        'F': ('S', 'E'),
        '.': None,
        'S': 'START',
    }
    x, y = start
    x += directions[curr_dir][0]
    y += directions[curr_dir][1]
    steps = 1

    while True:
        if grid[x][y] == '.':
            return None
        if grid[x][y] == 'S':
            return steps
        if opposite_dir[curr_dir] not in pipes[grid[x][y]]:
            return None
        curr_dir = pipes[grid[x][y]][0] if pipes[grid[x][y]][0] != opposite_dir[curr_dir] else pipes[grid[x][y]][1]
        x += directions[curr_dir][0]
        y += directions[curr_dir][1]
        steps += 1


grid = parse_input('input.txt')
start = find_start_position(grid)
grid = list(zip(*grid))
steps_per_initial_direction = []
for dirs in 'NSEW':
    steps_per_initial_direction.append(find_loop_len(start, dirs, grid))
steps_direction = list(filter(None, steps_per_initial_direction))
print(min(steps_direction) // 2)
