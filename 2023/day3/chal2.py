import re


def is_adjacent_to_symbol(x, y, schematic):
    symbol = '*'
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    adjacent_symbols = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(schematic) and 0 <= ny < len(schematic[0]):
            if schematic[nx][ny] == symbol:
                adjacent_symbols.append((nx, ny))
    return adjacent_symbols


def process_schematic(schematic):
    symbol_data = {}
    for i in range(len(schematic)):
        for match in re.finditer(r'\d+', schematic[i]):
            number = int(match.group())
            start_index, end_index = match.start(), match.end()
            for j in range(start_index, end_index):
                adjacent_symbols = is_adjacent_to_symbol(i, j, schematic)
                for symbol_location in adjacent_symbols:
                    if symbol_location not in symbol_data:
                        symbol_data[symbol_location] = {'count': 0, 'values': []}
                    if number not in symbol_data[symbol_location]['values']:
                        symbol_data[symbol_location]['count'] += 1
                        symbol_data[symbol_location]['values'].append(number)
    return symbol_data


# Read the engine schematic from the file
schematic = []
with open('input.txt', 'r') as file:
    for line in file:
        schematic.append(line.strip())

# Process the schematic and get symbol data
star_symbol_data = process_schematic(schematic)

# Print the data for each '*' symbol
# for location, data in star_symbol_data.items():
#     print(f"Symbol '*' at {location}: Count = {data['count']}, Values = {data['values']}")

# Rolling sum of products where count is 2
rolling_sum = 0
for data in star_symbol_data.values():
    if data['count'] == 2:
        rolling_sum += data['values'][0] * data['values'][1]

print(rolling_sum)