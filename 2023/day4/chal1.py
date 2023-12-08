rolling_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        _, game_data = line.split(':', 1)
        winning_numbers, drawn_numbers = game_data.split('|', 1)
        winning_numbers = [int(num) for num in winning_numbers.split()]
        drawn_numbers = [int(num) for num in drawn_numbers.split()]
        print(winning_numbers, drawn_numbers)
        counter = 0
        for num in drawn_numbers:
            if num in winning_numbers:
                counter += 1
        print(counter)
        if counter > 0:
            rolling_sum += 2 ** (counter - 1)
        print(rolling_sum)