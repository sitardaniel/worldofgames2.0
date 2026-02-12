import random
import requests
import json


def get_conversion_rate_usd_to_nis():
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=8MvokA3LxaytpwXUpxIZinVgKBE5fjbH7Sk94uoC"
    resp = requests.get(url)
    if resp.status_code != 200:
        print("error fetching conversion rate from api...")
        exit(1)
    my_data = json.loads(resp.content)
    return my_data['data']['ILS']


def get_money_interval(d, t):
    return t - (5 - d), t + (5 - d)


def get_guess_from_user(amount_of_usd):
    guessed_ils_price = float(input(f"please enter expected value in ILS of {amount_of_usd} USD"))
    return guessed_ils_price


def play(difficulty):
    conversion_rate = get_conversion_rate_usd_to_nis()
    draw_num = random.randint(1, 100)
    guessed_ils = get_guess_from_user(draw_num)
    correct_ils = conversion_rate * draw_num

    diff_abs = abs(correct_ils - guessed_ils)
    interval1, interval2 = get_money_interval(difficulty, conversion_rate)

    return interval1 < diff_abs < interval2 or interval2 < diff_abs < interval1
