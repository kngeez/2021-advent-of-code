def part_one():
    with open('input.txt', 'r') as file:
        for line in file:
            crab_positions = [int(i) for i in line.rstrip().split(',')]

    unique_positions = {}
    for position in crab_positions:
        if position in unique_positions:
            unique_positions[position] += 1
        else:
            unique_positions[position] = 1

    lowest_fuel = None
    lowest_fuel_position = None

    for to_position in unique_positions:
        fuel = 0

        for from_position in unique_positions:
            fuel += abs((from_position - to_position) * unique_positions[from_position])

        if lowest_fuel is None or fuel < lowest_fuel:
            lowest_fuel = fuel
            lowest_fuel_position = to_position

    print('---Part One---')
    print(f'Lowest Fuel: {lowest_fuel}')
    print(f'Lowest Fuel Position: {lowest_fuel_position}')


def get_crab_fuel(from_position, to_position):
    fuel = 0

    for step in range(1, abs(from_position - to_position) + 1):
        fuel += step

    return fuel


def part_two():
    with open('input.txt', 'r') as file:
        for line in file:
            crab_positions = [int(i) for i in line.rstrip().split(',')]

    unique_positions = {}
    for position in crab_positions:
        if position in unique_positions:
            unique_positions[position] += 1
        else:
            unique_positions[position] = 1

    lowest_fuel = None
    lowest_fuel_position = None

    for to_position in unique_positions:
        fuel = 0

        for from_position in unique_positions:
            fuel += abs(get_crab_fuel(from_position, to_position) * unique_positions[from_position])

        if lowest_fuel is None or fuel < lowest_fuel:
            lowest_fuel = fuel
            lowest_fuel_position = to_position

    print('---Part Two---')
    print(f'Lowest Fuel: {lowest_fuel}')
    print(f'Lowest Fuel Position: {lowest_fuel_position}')


part_one()
part_two()
