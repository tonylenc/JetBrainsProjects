import requests


cur = 'HNL'
web_page = requests.get(f'http://www.floatrates.com/daily/{cur}.json').json()


cache_ = {'USD', 'EUR'}
def_cur = input()

while True:
    cur_cur = input().upper()
    if not cur_cur:
        break
    cur_cash = float(input())

    print('Checking the cache...')
    if cur_cur in cache_:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache_.add(cur_cur)

    cur_exch = cur_cash * \
        web_page[cur_cur.lower()]['rate'] / web_page[def_cur.lower()]['rate']
    print(f'You received {round(cur_exch, 2)} {cur_cur}.')
