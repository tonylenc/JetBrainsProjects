from math import ceil, floor, log
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--type", default=None)
parser.add_argument("--payment", default=None)
parser.add_argument("--principal", default=None)
parser.add_argument("--periods", default=None)
parser.add_argument("--interest", default=None)


args = (
    parser.parse_args()
)  #  some kind of magic, but now args is an object of the class parser with attributes type, payment ...

what_received = [args.type, args.payment, args.principal, args.periods, args.interest]
what_have = list(filter(lambda x: x is not None, what_received))

enough = len(what_have) == 4 and args.type is not None
positive = all(map(lambda x: "-" not in x, what_have))
incorrect = False

if enough and positive:
    if args.type == "diff" and args.payment is None:
        command = "d"
    elif args.type == "annuity":
        if args.periods is None:
            command = "n"
        elif args.payment is None:
            command = "a"
        elif args.principal is None:
            command = "p"
        else:
            incorrect = True
    else:
        incorrect = True
else:
    incorrect = True


if not incorrect and command == "n":
    P = float(args.principal)
    A = float(args.payment)
    i_rate = float(args.interest)
    i = i_rate / 12 / 100

    n = ceil(log(A / (A - i * P), 1 + i))
    years, months = n // 12, n % 12

    if n % 12:
        print(f"It will take {years} years and {months} months to repay this loan!")
    else:
        print(f"It will take {years} years to repay this loan!")

    print(f"Overpayment = {ceil(A * n - P)}")

elif not incorrect and command == "a":
    P = float(args.principal)
    n = int(args.periods)
    i_rate = float(args.interest)
    i = i_rate / 12 / 100

    A = ceil(P * (i * (1 + i) ** n) / ((1 + i) ** n - 1))

    print(f"Your annuity payment = {A}!")
    print(f"Overpayment = {ceil(A * n - P)}")

elif not incorrect and command == "p":
    A = float(args.payment)
    n = int(args.periods)
    i_rate = float(args.interest)
    i = i_rate / 12 / 100

    P = floor(A * ((1 + i) ** n - 1) / (i * (1 + i) ** n))

    print(f"Your loan principal = {P}!")
    print(f"Overpayment = {ceil(A * n - P)}")

elif not incorrect and command == "d":
    P = float(args.principal)
    n = int(args.periods)
    i_rate = float(args.interest)
    i = i_rate / 12 / 100
    sm = 0

    for m in range(1, n + 1):
        Di = ceil(P / n + i * (P - P * (m - 1) / n))
        sm += Di
        print(f"Month {m}: payment is {Di}")

    print(f"\nOverpayment = {ceil(sm - P)}")

if incorrect:
    print("Incorrect parameters")