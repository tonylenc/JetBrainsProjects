import random
import operator


def welcome():
    print('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29''')
    ans = input()
    if ans.isdigit() and int(ans) in {1, 2}:
        {'1': first_level, '2': second_level}[ans]()
    else:
        print('Incorrect format.')
        welcome()


def first_level():
    cor_cnt = 0
    for _ in range(5):
        a, oper, b = gener_task()
        print(a, oper, b)

        while True:
            ans = input()
            if ans.isdigit() or ans.replace('-', '', 1).isdigit() and ans[0] == '-':
                break
            else:
                print("Incorrect format.")

        if int(ans) == solve_task(a, oper, b):
            print('Right!')
            cor_cnt += 1
        else:
            print('Wrong')

    print(
        f'Your mark is {cor_cnt}/5. Would you like to save the result? Enter yes or no.')
    if input() in {'yes', 'YES', 'y', 'Yes'}:
        want_to_save(cor_cnt, 1)


def second_level():
    cor_cnt = 0
    for _ in range(5):
        a = random.randrange(11, 30)
        print(a)

        while True:
            ans = input()
            if ans.isdigit():
                break
            else:
                print("Wrong format! Try again.")

        if int(ans) == a ** 2:
            print('Right!')
            cor_cnt += 1
        else:
            print('Wrong!')

    print(
        f'Your mark is {cor_cnt}/5. Would you like to save the result? Enter yes or no.')
    if input() in {'yes', 'YES', 'y', 'Yes'}:
        want_to_save(cor_cnt, 2)


def gener_task():
    a, oper, b = random.randrange(2, 10), random.choice(
        '+-*'), random.randrange(2, 10)
    return a, oper, b


def solve_task(a, oper, b):
    operation = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    return operation.get(oper)(int(a), int(b))


def want_to_save(cor_cnt, level):
    msg = ('simple operations with numbers 2-9',
           'integral squares of 11-29')[level - 1]

    name = input('What is your name?\n')
    my_file = open('results.txt', 'a')
    my_file.write(
        f'{name}: {cor_cnt}/5 in level {level} ({msg}).')
    my_file.close()

    print('The results are saved in "results.txt".')


welcome()