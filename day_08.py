# 1 = 2 digits
# 4 = 4 digits
# 7 = 3 digits
# 8 = 7 digits


def part_one():
    count = 0

    with open('input.txt', 'r') as file:
        for line in file:
            line = line.rstrip().split('|')

            four_digit = line[1].strip().split(' ')

            # print([four_digit])

            for signal_pattern in four_digit:
                if 2 <= len(signal_pattern) <= 4 or len(signal_pattern) == 7:
                    count += 1

    print('---Part One---')
    print(f'Total: {count}')
    print()


def decode_sequence(ten_digit_list):
    decoded_sequence = {}

    len_bucket = {5: set(), 6: set()}
    for sequence in ten_digit_list:
        sequence_len = len(sequence)
        sequence = ''.join(sorted(sequence))

        if sequence_len == 2:
            len_bucket[1] = sequence
            decoded_sequence[sequence] = 1
        elif sequence_len == 4:
            len_bucket[4] = sequence
            decoded_sequence[sequence] = 4
        elif sequence_len == 3:
            len_bucket[7] = sequence
            decoded_sequence[sequence] = 7
        elif sequence_len == 7:
            len_bucket[8] = sequence
            decoded_sequence[sequence] = 8
        else:
            len_bucket[sequence_len].add(sequence)

    # TOP LETTER
    top_letter = len_bucket[7]
    for letter in len_bucket[1]:
        top_letter = top_letter.replace(letter, '')

    # BOTTOM LETTER AND DECODE 9
    bottom_letter = ''
    for sequence in len_bucket[6]:
        letter_match_count = 0

        bottom_letter = sequence
        for letter in top_letter + len_bucket[4]:
            bottom_letter = bottom_letter.replace(letter, '')
            letter_match_count += 1

        if letter_match_count == 5 and len(bottom_letter) == 1:
            len_bucket[9] = sequence
            decoded_sequence[sequence] = 9
            len_bucket[6].remove(sequence)
            break

    # MIDDLE LETTER AND DECODE 3
    middle_letter = ''
    for sequence in len_bucket[5]:
        letter_match_count = 0

        middle_letter = sequence
        for letter in bottom_letter + len_bucket[7]:
            middle_letter = middle_letter.replace(letter, '')
            letter_match_count += 1

        if letter_match_count == 4 and len(middle_letter) == 1:
            decoded_sequence[sequence] = 3
            len_bucket[5].remove(sequence)
            break

    # DECODE 0 AND 6
    for sequence in len_bucket[6]:
        if middle_letter in sequence:
            decoded_sequence[sequence] = 6
        else:
            decoded_sequence[sequence] = 0

    # BOTTOM LEFT LETTER
    bottom_left_letter = 'abcdefg'
    for letter in len_bucket[9]:
        bottom_left_letter = bottom_left_letter.replace(letter, '')

    # DECODE 2 AND 5
    for sequence in len_bucket[5]:
        if bottom_left_letter in sequence:
            decoded_sequence[sequence] = 2
        else:
            decoded_sequence[sequence] = 5

    return decoded_sequence


def part_two():
    added_sum = 0

    with open('input.txt', 'r') as file:
        for line in file:
            line = line.rstrip().split('|')

            ten_digit = line[0].strip().split(' ')
            four_digit = line[1].strip().split(' ')

            # print([ten_digit, four_digit])

            decoded_sequences = decode_sequence(ten_digit)
            decoded_value = ''

            for signal_pattern in four_digit:
                decoded_value += str(decoded_sequences[''.join(sorted(signal_pattern))])

            # print(int(decoded_value))
            added_sum += int(decoded_value)

    print('---Part Two---')
    print(f'Total: {added_sum}')


part_one()
part_two()
