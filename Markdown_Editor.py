def help(key):
    return """Available formatters: plain bold italic header link inline-code new-line
Special command: !help !done"""


def header(key):
    while True:
        level = input("Level: ")
        if level not in {str(i) for i in range(1, 7)}:
            print("The level should be within the range of 1 to 6")
        else:
            level = int(level)
            break

    text = input("Text: ")

    return '\n' + "#" * level + ' ' + text + '\n'


def plain(key):
    return input("Text: ")


def bold(key):
    return f'**{input("Text: ")}**'


def italic(key):
    return f'*{input("Text: ")}*'


def inline_code(key):
    return f'`{input("Text: ")}`'


def new_line(key):
    return '\n'


def link(key):
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def for_list(our_type):

    while True:
        n = int(input('Number of rows: '))
        if n > 0:
            my_list = []
            for i in range(n):
                sign = {'ordered': f'{i+1}. ', 'unordered': '* '}[our_type]
                cur_el = input(f'Row #{i+1}: ')
                my_list.append(sign + cur_el + '\n')
            break
        else:
            print('The number of rows should be greater than zero')
    return ''.join(my_list)


def exit(my_str):
    with open('output.md', 'w') as f:
        f.write(my_str.lstrip())


commands = {
    "plain": plain,
    "bold": bold,
    "italic": italic,
    "header": header,
    "link": link,
    "inline-code": inline_code,
    "new-line": new_line,
    "ordered-list": for_list,
    "unordered-list": for_list,
    "!help": help
}

my_string = ""

while True:
    user_input = input("Choose a formatter: ")

    if user_input == '!done':
        exit(my_string)
        break

    if user_input not in commands:
        print("Unknown formatting type or command")
        continue

    key = {'ordered-list': 'ordered',
           'unordered-list': 'unordered'}.get(user_input, None)

    my_string += commands[user_input](key)
    print(my_string.lstrip())
