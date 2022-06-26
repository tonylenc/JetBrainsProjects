def draw(s):
    print("-" * 9)
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(s[3 * i + j], end=" ")
        print("|", end="")
        print()
    print("-" * 9)


def lines(s, el):
    el = el * 3
    cnt_line_hor = (s[0:3] == el) + (s[3:6] == el) + (s[6:9] == el)
    cnt_line_ver = (s[0:7:3] == el) + (s[1:8:3] == el) + (s[2:9:3] == el)
    cnt_line_diag = (s[0:9:4] == el) + (s[2:7:2] == el)

    return cnt_line_diag + cnt_line_hor + cnt_line_ver


s = "_" * 9


draw(s)
player = ["X", "O"]
switch = 0

while True:
    try:
        y, x = [int(i) - 1 for i in input().split()]
    except ValueError:
        print("You should enter numbers!")
    else:
        if not (4 > x + 1 > 0) or not (4 > y + 1 > 0):
            print("Coordinates should be from 1 to 3!")

        elif s[y * 3 + x] != "_":
            print("This cell is occupied! Choose another one!")

        else:
            s = s[: y * 3 + x] + player[switch] + s[y * 3 + x + 1 :]
            switch = (switch + 1) % 2
            draw(s)

    if lines(s, "X") == lines(s, "O") == 0 and "_" not in s:
        print("Draw")
        break
    elif lines(s, "X"):
        print("X wins")
        break
    elif lines(s, "O"):
        print("O wins")
        break
