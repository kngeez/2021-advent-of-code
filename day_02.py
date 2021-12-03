def part_one():
    horizontal_position = 0
    depth = 0

    with open('input.txt', 'r') as file:
        for line in file:
            data = line.rstrip().split(' ')

            movement_type = data[0]
            value = int(data[1])

            if movement_type == 'forward':
                horizontal_position += value
            elif movement_type == 'down':
                depth += value
            else:
                depth -= value

    print(f'''---Part One---
Horizontal: {horizontal_position}
Depth: {depth}
Multiply: {horizontal_position * depth}
''')


def part_two():
    horizontal_position = 0
    depth = 0
    aim = 0

    with open('input.txt', 'r') as file:
        for line in file:
            data = line.rstrip().split(' ')

            movement_type = data[0]
            value = int(data[1])

            if movement_type == 'forward':
                horizontal_position += value
                depth += value * aim
            elif movement_type == 'down':
                aim += value
            else:
                aim -= value

    print(f'''---Part Two---
Horizontal: {horizontal_position}
Depth: {depth}
Multiply: {horizontal_position * depth}
''')


part_one()
part_two()
