import re


def find_first_digit_or_word(s, number_words):
    matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))', s)
    # print(matches)
    for match in matches:
        if match.isdigit():
            return match
        if match.lower() in number_words:
            return number_words[match.lower()]
    return None


def find_last_digit_or_word(s, number_words):
    matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))', s)
    for match in reversed(matches):
        if match.isdigit():
            return match
        if match.lower() in number_words:
            return number_words[match.lower()]
    return None


def process_file(file_path):
    running_sum = 0
    number_words = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    with open(file_path, 'r') as file:
        for line in file:
            first_digit = find_first_digit_or_word(line, number_words)
            last_digit = find_last_digit_or_word(line, number_words)
            if first_digit is not None and last_digit is not None:
                two_digit_number = int(first_digit + last_digit)
                print(f"Processed line: {two_digit_number}")
                running_sum += two_digit_number
            else:
                print("No digits or written numbers found in line")
    print(f"Total sum is: {running_sum}")


process_file('input.txt')
