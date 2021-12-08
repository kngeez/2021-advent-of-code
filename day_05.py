class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(f'({self.x}, {self.y})')

    def __repr__(self):
        return str(f'({self.x}, {self.y})')

    def is_horizontal(self, other_x):
        return self.x == other_x

    def is_vertical(self, other_y):
        return self.y == other_y

    def get_line_points(self, other_point):
        points = [self]

        modifier = 1
        if self.is_horizontal(other_point.x):
            if self.y - other_point.y > 0:
                modifier = -1

            for delta in range(1, abs(self.y - other_point.y)):
                points.append(Point(self.x, self.y + (delta * modifier)))
        elif self.is_vertical(other_point.y):
            if self.x - other_point.x > 0:
                modifier = -1

            for delta in range(1, abs(self.x - other_point.x)):
                points.append(Point(self.x + (delta * modifier), self.y))
        else:
            return []

        points.append(other_point)

        return points


def part_one():
    point_count = {}

    with open('input.txt', 'r') as file:
        for line in file:
            data = line.rstrip().split(' ')
            point1 = data[0].split(',')
            point1 = Point(int(point1.pop(0)), int(point1.pop(0)))
            point2 = data[2].split(',')
            point2 = Point(int(point2.pop(0)), int(point2.pop(0)))

            for point in point1.get_line_points(point2):
                if str(point) in point_count:
                    point_count[str(point)] += 1
                else:
                    point_count[str(point)] = 1

    count = 0
    for point in point_count:
        if point_count[point] >= 2:
            count += 1

    print('---Part One---')
    print(f'Total: {count}')


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(f'({self.x}, {self.y})')

    def __repr__(self):
        return str(f'({self.x}, {self.y})')

    def is_horizontal(self, other_x):
        return self.x == other_x

    def is_vertical(self, other_y):
        return self.y == other_y

    def is_diagonal(self, other_x, other_y):
        return abs((other_y - self.y) / (other_x - self.x)) == 1

    def get_line_points(self, other_point):
        points = [self]

        modifier = 1
        if self.is_horizontal(other_point.x):
            if self.y - other_point.y > 0:
                modifier = -1

            for delta in range(1, abs(self.y - other_point.y)):
                points.append(Point2(self.x, self.y + (delta * modifier)))
        elif self.is_vertical(other_point.y):
            if self.x - other_point.x > 0:
                modifier = -1

            for delta in range(1, abs(self.x - other_point.x)):
                points.append(Point2(self.x + (delta * modifier), self.y))
        else:
            return []

        points.append(other_point)

        return points


def part_two():
    point_count = {}

    with open('input.txt', 'r') as file:
        for line in file:
            data = line.rstrip().split(' ')
            point1 = data[0].split(',')
            point1 = Point2(int(point1.pop(0)), int(point1.pop(0)))
            point2 = data[2].split(',')
            point2 = Point2(int(point2.pop(0)), int(point2.pop(0)))

            for point in point1.get_line_points(point2):
                if str(point) in point_count:
                    point_count[str(point)] += 1
                else:
                    point_count[str(point)] = 1

    count = 0
    for point in point_count:
        if point_count[point] >= 2:
            count += 1

    print('---Part Two---')
    print(f'Total: {count}')


part_one()
part_two()
