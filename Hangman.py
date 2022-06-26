import random
import string


win_games = 0
lose_games = 0


def menu():
    {"play": play, "results": results, "exit": exit}[
        input(
            'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: '
        )
    ]()


def results():
    global win_games, lose_games
    print(f"You won: {win_games} times.")
    print(f"You lost: {lose_games} times.")

    menu()


def exit():
    pass


def play():
    global win_games, lose_games

    my_words = ("python", "java", "swift", "javascript")
    word = random.choice(my_words)
    table = ["-" for i in range(len(word))]

    were_suggested = set()
    attempts = 8

    while attempts > 0:
        print()
        print(*table, sep="")
        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("Please, input a single letter.")
            continue
        elif letter not in string.ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        if letter in were_suggested:
            attempts -= 1
            print("You've already guessed this letter.")

        elif letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    table[i] = letter

        else:
            attempts -= 1
            print("That letter doesn't appear in the word.")

        were_suggested.add(letter)

        if word == "".join(table):
            print(f"\nYou guessed the word {word}!\nYou survived!")
            win_games += 1
            break
        elif not attempts:
            print("You lost!")
            lose_games += 1

    menu()


print("H A N G M A N")
menu()