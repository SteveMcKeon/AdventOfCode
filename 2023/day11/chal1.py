def find_hashes(grid):
    hash_coordinates = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                hash_coordinates.append((x, y))
    return hash_coordinates


def find_empty_rows_and_cols(grid):
    empty_rows = []
    empty_cols = []
    for row_idx, row in enumerate(grid):
        if '#' not in row:
            empty_rows.append(row_idx)
    transposed_grid = list(zip(*grid))
    for col_idx, col in enumerate(transposed_grid):
        if '#' not in col:
            empty_cols.append(col_idx)
    return empty_rows, empty_cols


def sum_of_lengths(hash_coords, empty_rows, empty_cols):
    i = 1
    running_total = 0
    for coord in hash_coords:
        for remaining_coord in hash_coords[i:]:
            x_dist = abs(coord[0] - remaining_coord[0])
            y_dist = abs(coord[1] - remaining_coord[1])
            for row in empty_rows:
                if min(coord[1], remaining_coord[1]) < row < max(coord[1], remaining_coord[1]):
                    y_dist += 1
            for col in empty_cols:
                if min(coord[0], remaining_coord[0]) < col < max(coord[0], remaining_coord[0]):
                    x_dist += 1
            running_total += x_dist + y_dist
        i += 1
    return running_total


def main():
    with open("input.txt", 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

    empty_rows, empty_cols = find_empty_rows_and_cols(grid)
    print(sum_of_lengths(find_hashes(grid), empty_rows, empty_cols))


if __name__ == '__main__':
    main()
