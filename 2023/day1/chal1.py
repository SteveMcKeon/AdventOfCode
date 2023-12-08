import re


def find_first_digit(s):
    match = re.search(r'\d', s)
    return match.group() if match else None


def find_last_digit(s):
    matches = re.findall(r'\d', s)
    return matches[-1] if matches else None


def process_file(file_path):
    running_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            first_digit = find_first_digit(line)
            last_digit = find_last_digit(line)
            if first_digit is not None and last_digit is not None:
                two_digit_number = int(first_digit + last_digit)
                print(f"Processed line: {two_digit_number}")
                running_sum += two_digit_number
            else:
                print("No digits found in line")
    print(f"Total sum is: {running_sum}")


process_file('input.txt')
