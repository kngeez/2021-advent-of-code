def part_one():
    days = 80
    lantern_fish_list = []

    with open('input.txt', 'r') as file:
        for line in file:
            lantern_fish_list = [int(i) for i in line.rstrip().split(',')]

    # print(f'Initial state: {lantern_fish_list}')

    for day in range(days):
        index = 0
        add_fish = 0

        for fish in lantern_fish_list:
            if fish == 0:
                add_fish += 1
                lantern_fish_list[index] = 6
            else:
                lantern_fish_list[index] -= 1
            index += 1

        for i in range(add_fish):
            lantern_fish_list.append(8)

        # print(f'After Day {day + 1}: {lantern_fish_list}')

    print('---Part One---')
    print(f'Total Lanternfish: {len(lantern_fish_list)}')
    print()


def part_two():
    days = 256

    with open('input.txt', 'r') as file:
        for line in file:
            initial_fish_list = [int(i) for i in line.rstrip().split(',')]

    fish_category = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for timer in initial_fish_list:
        fish_category[timer] += 1

    # print(f'Day 0: {fish_category}')

    for day in range(days):
        new_fish = fish_category[0]

        for timer in range(len(fish_category) - 1):
            fish_category[timer] = fish_category[timer + 1]

        fish_category[6] += new_fish
        fish_category[len(fish_category) - 1] = new_fish

        # print(f'Day {day + 1}: {fish_category}')

    total_fish = 0
    for fish in fish_category:
        total_fish += fish

    print('---Part Two---')
    print(f'Total Lanternfish: {total_fish}')


part_one()
part_two()
