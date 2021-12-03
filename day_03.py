def part_one():
    total = []

    with open('input.txt', 'r') as file:
        for bit in file.readline().rstrip():
            if bit == '0':
                total.append([1, 0])
            else:
                total.append([0, 1])

        for line in file:
            index = 0

            for bit in line.rstrip():
                if bit == '0':
                    total[index][0] += 1
                else:
                    total[index][1] += 1

                index += 1

    # reverse array order
    total = total[::-1]

    gamma_rate = 0
    epsilon_rate = 0
    for index in range(0, len(total)):
        if total[index][0] > total[index][1]:
            gamma_rate += 0 * 2 ** index
            epsilon_rate += 1 * 2 ** index
        else:
            gamma_rate += 1 * 2 ** index
            epsilon_rate += 0 * 2 ** index

    print(f'''---Part One---
Gamma Rate: {gamma_rate}
Epsilon Rate: {epsilon_rate}
Mulitply: {gamma_rate * epsilon_rate}
''')


def traverse_most_common_list(position, binary_list):
    if len(binary_list) == 1:
        return binary_list[0]
    else:
        zero_list = []
        one_list = []

        for binary in binary_list:
            if binary[position] == '0':
                zero_list.append(binary)
            else:
                one_list.append(binary)

        if len(one_list) >= len(zero_list):
            return traverse_most_common_list(position + 1, one_list)
        else:
            return traverse_most_common_list(position + 1, zero_list)


def traverse_least_common_list(position, binary_list):
    if len(binary_list) == 1:
        return binary_list[0]
    else:
        zero_list = []
        one_list = []

        for binary in binary_list:
            if binary[position] == '0':
                zero_list.append(binary)
            else:
                one_list.append(binary)

        if len(zero_list) <= len(one_list):
            return traverse_least_common_list(position + 1, zero_list)
        else:
            return traverse_least_common_list(position + 1, one_list)


def part_two():
    binaries = []
    with open('input.txt', 'r') as file:
        for line in file:
            binaries.append(line.rstrip())

    oxygen_generator_rating = traverse_most_common_list(0, binaries)
    co2_scrubber_rating = traverse_least_common_list(0, binaries)

    print(f'''---Part Two---
Oxygen Generator Rating: {[oxygen_generator_rating, int(oxygen_generator_rating, 2)]}
CO2 Scrubber Rating: {[co2_scrubber_rating, int(co2_scrubber_rating, 2)]}
Mulitply: {int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)}
''')


part_one()
part_two()
