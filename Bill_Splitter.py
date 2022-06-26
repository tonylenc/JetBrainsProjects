import random

guests_numb = int(input("Enter the number of friends joining (including you):\n"))

if guests_numb <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    guests_list = [input() for i in range(guests_numb)]

    print()
    total_bill = int(input("Enter the total bill value:\n"))

    print()
    lucky_feat = input(
        'Do you want to use the "Who is lucky?" feature? Write Yes/No:\n'
    )

    print()
    if lucky_feat == "Yes":
        lucky_pers = random.choice(guests_list)
        print(f"{lucky_pers} is the lucky one!")

        print()
        guests_dict = {
            i: round(total_bill / (len(guests_list) - 1), 2) if i != lucky_pers else 0
            for i in guests_list
        }
        print(guests_dict)
    else:
        print("No one is going to be lucky")

        print()
        guests_dict = {i: round(total_bill / len(guests_list), 2) for i in guests_list}

        print(guests_dict)
