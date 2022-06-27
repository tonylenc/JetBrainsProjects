def print_msg(n):
    msg = (
        "The number of pencils should be numeric\n",
        "The number of pencils shouls be positive\n",
        "Choose between John and Jack\n",
        "Possible values: '1', '2' or '3'\n",
        "Too many pencils were taken\n",
    )
    return msg[n]


def take_valid_start_numb():
    pen_numb = input("How many pencils would you like to use?\n")
    while True:
        if not pen_numb.isdigit():
            pen_numb = input(print_msg(0))
            continue

        pen_numb = int(pen_numb)
        if pen_numb < 0:
            pen_numb = input(print_msg(0))
        elif not pen_numb:
            pen_numb = input(print_msg(1))
        else:
            return pen_numb


def take_valid_name():
    name = input("Who will be the first (John, Jack):\n")
    while True:
        if name in {"John", "Jack"}:
            return name
        name = input(print_msg(2))


def valid_reduce(pen_numb):
    pen_red = input()
    while True:
        if not pen_red.isdigit():
            pen_red = input(print_msg(3))
            continue

        pen_red = int(pen_red)
        if pen_red not in {1, 2, 3}:
            pen_red = input(print_msg(3))
        elif pen_red > pen_numb:
            pen_red = input(print_msg(4))
        else:
            return pen_red


def who_starts(who_first):
    players = ["John", "Jack"]
    players.remove(who_first)
    players = [who_first] + players

    return players


def print_turn(pen_numb, players):
    sign = ":"
    if players[0] == "John":
        sign = "!"
    print("|" * pen_numb)
    print(f"{players[0]}'s turn{sign}")


def correct_reduce(pen_numb):
    for i in range(1, 4):
        if (pen_numb - i - 1) % 4 == 0:
            print(i)
            return i
    else:
        print(1)
        return 1


pen_numb = take_valid_start_numb()
who_first = take_valid_name()
players = who_starts(who_first)


while pen_numb > 0:
    print_turn(pen_numb, players)
    if players[0] == "John":
        pen_numb -= valid_reduce(pen_numb)
    else:
        pen_numb -= correct_reduce(pen_numb)

    players = players[::-1]

print(f"{players[0]} won!")
