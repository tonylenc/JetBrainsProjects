import random


def generate_domino():
    all_domino = [[i, j] for j in range(0, 7) for i in range(j, 7)]
    random.shuffle(all_domino)
    return all_domino


def take_and_give(where, amount):
    to = [where.pop() for _ in range(amount)]
    return where, to


def count_numb(n, my_list):
    cnt = 0
    for i in my_list:
        cnt += i.count(n)
    return cnt


def description(stock_pieces, computer_pieces, domino_snake, player_pieces):
    print("=" * 70)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}")
    print()
    print(*domino_snake, sep="")
    print()
    print("Your pieces:")
    for i in range(len(player_pieces)):
        print(f"{i + 1}:{player_pieces[i]}")
    print()


def choose_status(player_pieces, computer_pieces, left, right, stock_pieces, turn):
    status = [
        "Status: Computer is about to make a move. Press Enter to continue...",
        "Status: It's your turn to make a move. Enter your command.",
        "Status: The game is over. You won!",
        "Status: The game is over. The computer won!",
        "Status: The game is over. It's a draw!",
    ]
    flag = False

    if len(player_pieces) == 0:
        turn = 2
    elif len(computer_pieces) == 0:
        turn = 3
    elif (
        left == right
        and count_numb(left, player_pieces)
        + count_numb(left, computer_pieces)
        + count_numb(left, stock_pieces)
        == 0
    ):
        turn = 4
    else:
        flag = True

    print(status[turn])

    return flag, turn


def who_starts(computer, player):
    mx = [-1, -1]
    giver = None

    for i in computer:
        if i[0] == i[1] and i[0] > mx[0]:
            mx = i
            giver = "computer"

    for i in player:
        if i[0] == i[1] and i[0] > mx[0]:
            mx = i
            giver = "player"

    return giver, mx


def preparing():
    while True:
        all_domino = generate_domino()

        all_domino, stock_pieces = take_and_give(all_domino, 14)
        all_domino, computer_pieces = take_and_give(all_domino, 7)
        all_domino, player_pieces = take_and_give(all_domino, 7)

        giver, domino_snake = who_starts(computer_pieces, player_pieces)

        if giver is not None:
            if giver == "computer":
                computer_pieces.remove(domino_snake)
                winner = "player"
                turn = 1
            else:
                player_pieces.remove(domino_snake)
                winner = "computer"
                turn = 0

            domino_snake = [domino_snake]
            game(stock_pieces, computer_pieces, domino_snake, player_pieces, turn)
            break


def game(stock_pieces, computer_pieces, domino_snake, player_pieces, turn):
    left = domino_snake[0][0]
    right = domino_snake[-1][1]

    description(stock_pieces, computer_pieces, domino_snake, player_pieces)

    flag, turn = choose_status(
        player_pieces, computer_pieces, left, right, stock_pieces, turn
    )

    if turn and flag:
        while True:
            try:
                command = int(input())
                destination = command > 0
                piece = player_pieces[abs(command) - 1]
            except:
                print("Invalid input. Please try again.")
            else:
                if command == 0:
                    if stock_pieces:
                        player_pieces += [stock_pieces.pop()]
                    break

                if destination:
                    if right == piece[0]:
                        domino_snake = domino_snake + [piece]
                    elif right == piece[1]:
                        domino_snake = domino_snake + [piece[::-1]]
                    else:
                        print("Illegal move. Please try again.")
                        continue
                else:
                    if left == piece[1]:
                        domino_snake = [piece] + domino_snake
                    elif left == piece[0]:
                        domino_snake = [piece[::-1]] + domino_snake
                    else:
                        print("Illegal move. Please try again.")
                        continue

                player_pieces.remove(piece)
                break
    elif flag:
        for l, r in computer_pieces:
            if l == right:
                domino_snake = domino_snake + [[l, r]]
                computer_pieces.remove([l, r])
                break
            elif l == left:
                domino_snake = [[r, l]] + domino_snake
                computer_pieces.remove([r, l][::-1])
                break
            elif r == right:
                domino_snake = domino_snake + [[r, l]]
                computer_pieces.remove([r, l][::-1])
                break
            elif r == left:
                domino_snake = [[l, r]] + domino_snake
                computer_pieces.remove([l, r])
                break
        else:
            if stock_pieces:
                computer_pieces += [stock_pieces.pop()]

        input()

    if len(domino_snake) > 6:
        if "..." in domino_snake and len(domino_snake) == 8:
            del domino_snake[4]
        domino_snake[3] = "..."

    if turn in {0, 1}:
        turn = (turn + 1) % 2
        game(stock_pieces, computer_pieces, domino_snake, player_pieces, turn)


preparing()
