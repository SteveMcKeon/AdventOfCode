import re


def is_adjacent_to_symbol(x, y, schematic):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(schematic) and 0 <= ny < len(schematic[0]):
            if schematic[nx][ny] in '*#+$/=@%&-':
                return True
    return False


def sum_part_numbers(schematic):
    sum_parts = 0
    for i in range(len(schematic)):
        for match in re.finditer(r'\d+', schematic[i]):
            number = int(match.group())
            start_index = match.start()
            if any(is_adjacent_to_symbol(i, j, schematic) for j in range(start_index, start_index + len(match.group()))):
                sum_parts += number
    return sum_parts


# Read the engine schematic from the file
schematic = []
with open('input.txt', 'r') as file:
    for line in file:
        schematic.append(line.strip())

# Calculate the sum of all the part numbers
sum_parts = sum_part_numbers(schematic)
print(sum_parts)
