import operator


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += " ... lazy"

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += " ... very lazy"

    if (v1 == 0 or v2 == 0) and v3 in ["*", "+", "-"]:
        msg += " ... very, very lazy"

    if msg:
        msg = "You are" + msg
        print(msg)


def is_one_digit(v):
    return abs(v) < 10 and v.is_integer()


def for_res(res):
    msg_ = [
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)",
    ]
    msg_index = 0

    if is_one_digit(res):
        while True:
            print(msg_[msg_index])

            if input() == "y":
                if msg_index < 2:
                    msg_index += 1

                else:
                    return "y"
            else:
                return "n"
    return "y"


M = 0

while True:
    print("Enter an equation")
    x, sign, y = input().split()

    try:
        x = x.replace("M", str(M))
        y = y.replace("M", str(M))
        x, y = float(x), float(y)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue
    else:
        try:
            check(x, y, sign)

            res = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv,
            }.get(sign)(x, y)
            print(res)

            while True:
                print("Do you want to store the result? (y / n):")
                in_put = input()
                if in_put in ("y", "n"):
                    break

            if in_put == "y" and for_res(res) == "y":
                M = res

            while True:
                print("Do you want to continue calculations? (y / n):")
                in_put = input()
                if in_put in ("y", "n"):
                    break

            if in_put == "n":
                break
        except TypeError:
            print(
                "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
            )
        except ZeroDivisionError:
            print("Yeah... division by zero. Smart move...")
