def generate_sequences(history):
    sequences = [history]
    while True:
        new_sequence = [sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)]
        sequences.append(new_sequence)
        if all(v == 0 for v in new_sequence):
            return sequences


def find_next_value(history):
    sequences = generate_sequences(history)
    running_sum = 0
    for i in range(len(sequences) - 1, 0, -1):
        running_sum = ((sequences[i-1][0]) - running_sum)
        # print(f"running_sum: {running_sum}")
    return running_sum


total_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        history = list(map(int, line.split()))
        next_value = find_next_value(history)
        # print(f"Next value for {history}: {next_value}")
        total_sum += next_value

print(f"Total sum: {total_sum}")
