class NegativeZeroResultError(Exception):
    pass


class NotInBordersError(Exception):
    pass


def draw_plate(my_plate, cell_size):
    col = len(my_plate[0])
    row = len(my_plate)

    print(" " * len_int(row), "", sep=(col * (cell_size + 1) + 3) * "-")

    for i in range(row):
        print(
            " " * (len_int(row) - len_int(row - i)) + str(row - i), "| ", sep="", end=""
        )
        print(*my_plate[i], end="")
        print(" |")

    print(" " * len_int(row), "", sep=(col * (cell_size + 1) + 3) * "-")
    print(
        " " * (3 + len_int(row) - 1),
        " " * (3 + len_int(row) - 1),
        sep=" ".join(
            [" " * (cell_size - len_int(i + 1)) + str(i + 1) for i in range(col)]
        ),
    )

    for i in range(row):
        for j in range(col):
            if "X" in my_plate[i][j]:
                my_plate[i][j] = " " * (cell_size - 1) + "*"
            elif "*" not in my_plate[i][j]:
                my_plate[i][j] = "_" * cell_size


def len_int(n):
    return len(str(n))


def take_valid_start(num, col=None, row=None):
    msg = ("Enter your board dimensions: ", "Enter the knight's starting position: ")

    while True:
        print(msg[num], end="")
        try:
            x, y = [int(i) for i in input().split()]
            if x <= 0 or y <= 0:
                raise NegativeZeroResultError
            if num == 1 and (x > col or y > row):
                raise NotInBordersError

            return x, y
        except ValueError:
            print("Invalid dimensions!")
        except NegativeZeroResultError:
            print("Invalid dimensions!")
        except NotInBordersError:
            print("Invalid dimensions!")


def mark_possible_moves(my_plate, x, y, cell_size):
    col = len(my_plate[0])
    row = len(my_plate)

    possible_moves = set()

    for i in range(row):
        for j in range(col):
            if (x - j) ** 2 + (y - i) ** 2 == 5:
                if "*" in my_plate[i][j]:
                    continue

                possible_moves.add((j, i))
                my_plate[i][j] = " " * (cell_size - 1) + str(
                    count_possible_moves(my_plate, j, i)
                )

    return possible_moves


def count_possible_moves(my_plate, x, y):
    col = len(my_plate[0])
    row = len(my_plate)
    cnt = -1

    for i in range(row):
        for j in range(col):
            if (x - j) ** 2 + (y - i) ** 2 == 5 and "*" not in my_plate[i][j]:
                cnt += 1

    return cnt


def take_valid_move(possible_moves, row):
    welcome = ""
    while True:
        print(welcome + "Enter your next move: ", end="")
        try:
            x, y = [int(i) for i in input().split()]
            if x <= 0 or y <= 0:
                raise NegativeZeroResultError
            if (x - 1, row - y) not in possible_moves:
                raise NotInBordersError

            return x - 1, row - y
        except ValueError:
            welcome = "Invalid move! "
        except NegativeZeroResultError:
            welcome = "Invalid move! "
        except NotInBordersError:
            welcome = "Invalid move! "


def are_empty_cells(my_plate):
    for i in my_plate:
        for j in i:
            if "_" in j:
                return True
    return False


def game(my_plate, cell_size, possible_moves, moves):
    row = len(my_plate)

    x_cur, y_cur = take_valid_move(possible_moves, row)

    my_plate[y_cur][x_cur] = " " * (cell_size - 1) + "X"

    possible_moves = mark_possible_moves(my_plate, x_cur, y_cur, cell_size)

    draw_plate(my_plate, cell_size)
    print()

    moves += 1

    if possible_moves:
        game(my_plate, cell_size, possible_moves, moves)
    elif are_empty_cells(my_plate):
        print("No more possible moves!")
        print(f"Your knight visited {moves} squares!")
    else:
        print("What a great tour! Congratulations!")


def start():
    col, row = take_valid_start(0)
    cell_size = len_int(col * row)

    my_plate = [["_" * cell_size for _ in range(col)] for _ in range(row)]

    x_st, y_st = take_valid_start(1, col, row)
    x_st -= 1
    y_st = row - y_st

    my_plate[y_st][x_st] = " " * (cell_size - 1) + "X"

    possible_moves = mark_possible_moves(my_plate, x_st, y_st, cell_size)

    moves = 1

    while True:
        in_put = input("Do you want to try the puzzle? (y/n): ")
        if in_put not in {"y", "n"}:
            print("Invalid input!")
        else:
            break

    win_plate = are_solutions(row, col, y_st, x_st)

    if not win_plate:
        print("No solution exists!")
    elif in_put == "n":
        show_solution(win_plate, cell_size)
    elif in_put == "y":
        draw_plate(my_plate, cell_size)
        print()

        if possible_moves:
            game(my_plate, cell_size, possible_moves, moves)
        elif are_empty_cells(my_plate):
            print("No more possible moves!")
            print(f"Your knight visited {moves} squares!")
        else:
            print("What a great tour! Congratulations!")


def find_solution(my_plate, y, x, cnt):
    row, col = len(my_plate), len(my_plate[0])
    if check_smt(my_plate):
        for i in range(row):
            win_plate = None
            for j in range(col):
                if (x - j) ** 2 + (y - i) ** 2 == 5 and my_plate[i][j] == "_":
                    cnt += 1
                    my_plate[i][j] = "X"
                    my_plate[y][x] = str(cnt)
                    win_plate = find_solution(my_plate, i, j, cnt)
                    if win_plate:
                        return win_plate
                    cnt -= 1
                    my_plate[i][j] = "_"
                    my_plate[y][x] = "X"
            if win_plate:
                return win_plate
    else:
        cnt += 1
        my_plate[y][x] = str(cnt)
        return my_plate


def check_smt(my_plate):
    for i in my_plate:
        if "_" in i:
            return True
    return False


def are_solutions(row, col, y, x):
    my_plate = [["_" for j in range(col)] for i in range(row)]
    cnt = 0
    my_plate[y][x] = "X"

    return find_solution(my_plate, y, x, cnt)


def show_solution(win_plate, cell_size):
    print()
    print("Here's the solution!")
    win_plate = [
        [
            " " * (cell_size - len_int(win_plate[i][j])) + str(win_plate[i][j])
            for j in range(len(win_plate[0]))
        ]
        for i in range(len(win_plate))
    ]
    draw_plate(win_plate, cell_size)


start()
