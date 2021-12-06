class Board:
    def __init__(self):
        self.board = []

    def add_row(self, row):
        self.board.append(row)

    def check_number(self, draw_number):
        row_count = 0
        for row in self.board:
            if draw_number in row:
                self.board[row_count].remove(draw_number)
            row_count += 1

    def check_win(self):
        count_empty = 0

        for row in self.board:
            if len(row) == 0:
                count_empty += 1

        if count_empty == 1:
            return True

        return False

    def get_score(self, number_draw):
        score = 0
        for index in range(5):
            for number in self.board[index]:
                score += int(number)

        return score * int(number_draw)

    def print_board(self):
        for row in self.board:
            print(row)
        print()


def part_one():
    # Set Up Boards
    with open('input.txt', 'r') as file:
        draw_numbers = next(file).rstrip().split(',')
        next(file)

        boards = []
        current_board = Board()
        columns = [set(), set(), set(), set(), set()]

        for line in file:
            line = line.rstrip()

            if line == '':
                for column in columns:
                    current_board.add_row(column)
                boards.append(current_board)
                current_board = Board()
                columns = [set(), set(), set(), set(), set()]
            else:
                board_row = line.split(' ')
                row_set = set()

                column_number = 0
                for number in board_row:
                    if number != '':
                        row_set.add(number)
                        columns[column_number].add(number)
                        column_number += 1
                current_board.add_row(row_set)

        for column in columns:
            current_board.add_row(column)
        boards.append(current_board)

    # print(f'Draw Numbers: {draw_numbers}')
    # for board in boards:
    #     board.print_board()

    # Play Game
    print(f'---Part One---')
    win_found = False

    for number in draw_numbers:
        for board in boards:
            board.check_number(number)
            if board.check_win():
                print(f'Score: {board.get_score(number)}')
                win_found = True
                break
        if win_found:
            break


def part_two():
    # Set Up Boards
    with open('input.txt', 'r') as file:
        draw_numbers = next(file).rstrip().split(',')
        next(file)

        boards = []
        current_board = Board()
        columns = [set(), set(), set(), set(), set()]

        for line in file:
            line = line.rstrip()

            if line == '':
                for column in columns:
                    current_board.add_row(column)
                boards.append(current_board)
                current_board = Board()
                columns = [set(), set(), set(), set(), set()]
            else:
                board_row = line.split(' ')
                row_set = set()

                column_number = 0
                for number in board_row:
                    if number != '':
                        row_set.add(number)
                        columns[column_number].add(number)
                        column_number += 1
                current_board.add_row(row_set)

        for column in columns:
            current_board.add_row(column)
        boards.append(current_board)

    # print(f'Draw Numbers: {draw_numbers}')
    # for board in boards:
    #     board.print_board()

    # Play Game
    print()
    print(f'---Part Two---')

    last_winning_board = ''
    last_winning_number = ''

    for number in draw_numbers:
        board_index = 0
        winning_board = ''

        for board in boards:
            board.check_number(number)
            if board.check_win():
                last_winning_board = board
                last_winning_number = number
                winning_board = board_index

            board_index += 1

        if winning_board != '':
            boards.pop(winning_board)

    # last_winning_board.print_board()
    # print(last_winning_number)
    print(f'Score: {last_winning_board.get_score(last_winning_number)}')


part_one()
part_two()
