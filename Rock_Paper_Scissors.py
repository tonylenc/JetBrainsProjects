import random


class InvalidInput(Exception):
    pass


def take_check_input(name, ratings, options):
    while True:
        try:
            user_option = input()
            if user_option not in {'!exit', '!rating', *options}:
                raise InvalidInput
            elif user_option == '!rating':
                print(f'Your rating: {ratings[name]}')
            else:
                break

        except InvalidInput:
            print('Invalid Input')

    return user_option


def take_data_from_file():
    my_file = open('rating.txt', 'r')
    ratings = {}
    for i in my_file:
        cur_line = i.replace('\n', '').split()
        ratings[cur_line[0]] = int(cur_line[1])

    my_file.close()
    return ratings


def take_options():
    print('What format of the game you want(3, 5, 7, 9, 11, 15')

    while True:
        try:
            n = int(input())
        except:
            print('Incorrect input')
        else:
            break

    print("Okay, let's start")
    if n == 3:
        return ['rock', 'paper', 'scissors']
    if n == 5:
        return ['rock', 'paper', 'scissors', 'spock', 'lizard']
    if n == 7:
        return ['rock', 'water', 'air', 'paper', 'sponge', 'scissors', 'fire']
    if n == 9:
        return ['rock', 'gun', 'water', 'air', 'paper', 'sponge', 'human', 'scissors']
    if n == 11:
        return ['rock', 'gun', 'devil', 'water', 'air', 'paper', 'sponge', 'wolf', 'human', 'scissors', 'fire']
    if n == 15:
        return ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree',
                'human', 'snake', 'scissors', 'fire']


def determine_res(options, comp_option, user_option):
    dif = options.index(comp_option) - options.index(user_option)

    if len(options) // 2 >= dif > 0:
        return 1
    if not dif:
        return 0
    return 2


def start():
    ratings = take_data_from_file()

    name = input('Enter your name: ')
    print('Hello,', name)

    ratings[name] = ratings.get(name, 0)

    game(ratings, name)


def game(ratings, name):
    options = take_options()
    user_option = take_check_input(name, ratings, options)

    while user_option != '!exit':
        comp_option = random.choice(options)

        res = ('There is a draw ({})'.format(comp_option), 'Sorry, but the computer chose {}'.format(
            comp_option), 'Well done. The computer chose {} and failed'.format(comp_option))
        res_add = (50, 0, 100)

        n_res = determine_res(options, comp_option, user_option)

        ratings[name] += res_add[n_res]
        print(res[n_res])

        user_option = take_check_input(name, ratings, options)

    print('Bye!')


start()
