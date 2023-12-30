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


def find_loop_cords(start, curr_dir, grid):
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
    loop_cords = [start]
    x, y = start
    x += directions[curr_dir][0]
    y += directions[curr_dir][1]
    loop_cords.append((x, y))
    while True:
        if grid[x][y] == '.':
            return None
        if grid[x][y] == 'S':
            return loop_cords
        if opposite_dir[curr_dir] not in pipes[grid[x][y]]:
            return None
        curr_dir = pipes[grid[x][y]][0] if pipes[grid[x][y]][0] != opposite_dir[curr_dir] else pipes[grid[x][y]][1]
        x += directions[curr_dir][0]
        y += directions[curr_dir][1]
        loop_cords.append((x, y))


grid = parse_input('input.txt')
start = find_start_position(grid)
grid = list(zip(*grid))
final_cords_w_dir = None
for dirs in 'NSEW':
    loop_cords = find_loop_cords(start, dirs, grid)
    if loop_cords:
        final_cords_w_dir = loop_cords
        break

clear_area = []
for x, line in enumerate(grid):
    new_line = []
    for y, char in enumerate(line):
        if (x, y) in final_cords_w_dir:
            new_line.append(char)
        else:
            new_line.append('0')
    clear_area.append(new_line)
clear_area = list(zip(*clear_area))

tiles = 0
for y, line in enumerate(clear_area):
    count_tiles = False
    for x, char in enumerate(line):
        if char != '0':
            if (char == 'F' or char == '7' or char == '|' or char == 'S') and not count_tiles:
                count_tiles = True
            elif (char == 'F' or char == '7' or char == '|' or char == 'S') and count_tiles:
                count_tiles = False
        if char == '0' and count_tiles:
            tiles += 1
print(tiles)
