from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


with open('input.txt', 'r') as file:
    lines = file.readlines()

directions = lines[0].strip()
node_mappings = {}

for line in lines[2:]:
    node, mapping = line.strip().split(' = ')
    left, right = mapping.strip('()').split(', ')
    node_mappings[node] = (left, right)

starting_nodes = [node for node in node_mappings if node.endswith('A')]

step_counts = []
for starting_node in starting_nodes:
    current_node = starting_node
    direction_index = 0
    step_count = 0

    while not current_node.endswith('Z'):
        direction = directions[direction_index]
        current_node = node_mappings[current_node][0] if direction == 'L' else node_mappings[current_node][1]
        step_count += 1
        direction_index = (direction_index + 1) % len(directions)

    step_counts.append(step_count)

resulting_lcm = step_counts[0]
for count in step_counts[1:]:
    resulting_lcm = lcm(resulting_lcm, count)

print(f"LCM of step counts: {resulting_lcm}")
