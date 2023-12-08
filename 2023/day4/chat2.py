rolling_sum = 0
card_number = 0
my_cards = {key: 0 for key in range(1, 190)}
with open('input.txt', 'r') as file:
    for line in file:
        card_number += 1
        my_cards[card_number] += 1
        _, game_data = line.split(':', 1)
        winning_numbers, drawn_numbers = game_data.split('|', 1)
        winning_numbers = [int(num) for num in winning_numbers.split()]
        drawn_numbers = [int(num) for num in drawn_numbers.split()]
        # print(winning_numbers, drawn_numbers)
        wins = 0
        for num in drawn_numbers:
            if num in winning_numbers:
                wins += 1
        i = 1
        # print(wins)
        while wins:
            my_cards[card_number + i] += my_cards[card_number]
            wins -= 1
            i += 1
        # print(my_cards)
total_sum = sum(my_cards.values())
print(total_sum)
