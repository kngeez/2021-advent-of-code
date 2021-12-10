def part_one():
    heightmap = []

    with open('input.txt', 'r') as file:
        for line in file:
            heightmap.append([int(i) for i in list(line.rstrip())])

    # for line in heightmap:
    #     print(line)

    lowest_points = []

    heightmap_index = 0
    for row in heightmap:
        for index in range(len(row)):
            current_value = row[index]
            lowest_value = True

            # check above if exists
            if heightmap_index > 0:
                if current_value >= heightmap[heightmap_index - 1][index]:
                    lowest_value = False

            # check below if exists
            if heightmap_index < len(heightmap) - 1:
                if current_value >= heightmap[heightmap_index + 1][index]:
                    lowest_value = False

            # check left if exists
            if index > 0:
                if current_value >= heightmap[heightmap_index][index - 1]:
                    lowest_value = False

            # check right if exists
            if index < len(row) - 1:
                if current_value >= heightmap[heightmap_index][index + 1]:
                    lowest_value = False

            if lowest_value:
                lowest_points.append(current_value)

        heightmap_index += 1

    risk_sum = sum(point + 1 for point in lowest_points)

    print('---Part One---')
    print(f'Lowest Points: {lowest_points}')
    print(f'Risk Sum: {risk_sum}')
    print()


part_one()
