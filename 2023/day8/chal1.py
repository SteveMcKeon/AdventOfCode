with open('input.txt', 'r') as file:
    lines = file.readlines()

directions = lines[0].strip()
node_mappings = {}

for line in lines[2:]:
    node, mapping = line.strip().split(' = ')
    left, right = mapping.strip('()').split(', ')
    node_mappings[node] = (left, right)

current_node = 'AAA'
direction_index = 0
step_count = 0

while current_node != 'ZZZ':
    direction = directions[direction_index]
    current_node = node_mappings[current_node][0] if direction == 'L' else node_mappings[current_node][1]
    direction_index = (direction_index + 1) % len(directions)
    step_count += 1

print(step_count)
