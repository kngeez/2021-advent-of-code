class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(f'({self.x}, {self.y})')

    def __repr__(self):
        return str(f'({self.x}, {self.y})')

    def is_horizontal(self, other_point):
        return self.x == other_point.x

    def is_vertical(self, other_point):
        return self.y == other_point.y

    def is_diagonal(self, other_point):
        return abs((other_point.y - self.y) / (other_point.x - self.x)) == 1

    def get_horizontal_points(self, other_point):
        points = [self]
        modifier = 1

        if self.y - other_point.y > 0:
            modifier = -1

        for delta in range(1, abs(self.y - other_point.y)):
            points.append(Point(self.x, self.y + (delta * modifier)))

        points.append(other_point)

        return points

    def get_vertical_points(self, other_point):
        points = [self]
        modifier = 1

        if self.x - other_point.x > 0:
            modifier = -1

        for delta in range(1, abs(self.x - other_point.x)):
            points.append(Point(self.x + (delta * modifier), self.y))

        points.append(other_point)

        return points

    def get_diagonal_points(self, other_point):
        points = [self]

        if self.x < other_point.x:
            x_points = range(self.x + 1, other_point.x)
        else:
            x_points = range(self.x - 1, other_point.x, -1)

        if self.y < other_point.y:
            y_points = range(self.y + 1, other_point.y)
        else:
            y_points = range(self.y - 1, other_point.y, -1)

        for index in range(len(x_points)):
            points.append(Point(x_points[index], y_points[index]))

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

            points = []

            if point1.is_horizontal(point2):
                points = point1.get_horizontal_points(point2)
            elif point1.is_vertical(point2):
                points = point1.get_vertical_points(point2)

            for point in points:
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
    print()


def part_two():
    point_count = {}

    with open('input.txt', 'r') as file:
        for line in file:
            data = line.rstrip().split(' ')
            point1 = data[0].split(',')
            point1 = Point(int(point1.pop(0)), int(point1.pop(0)))
            point2 = data[2].split(',')
            point2 = Point(int(point2.pop(0)), int(point2.pop(0)))

            points = []

            if point1.is_horizontal(point2):
                points = point1.get_horizontal_points(point2)
            elif point1.is_vertical(point2):
                points = point1.get_vertical_points(point2)
            elif point1.is_diagonal(point2):
                points = point1.get_diagonal_points(point2)

            for point in points:
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
