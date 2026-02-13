import os
import subprocess
import random
from time import sleep


def generate_sequence(difficulty):
    list_of_num = []
    for i in range(difficulty):
        list_of_num.append(random.randint(1, 101))
    return list_of_num


def get_list_from_user(difficulty):
    list_of_unum = []
    for i in range(difficulty):
        list_of_unum.append(input("Please enter a number:"))
    return list_of_unum


def is_list_equal(list_of_num, list_of_unum):
    l1 = list_of_num
    l2 = list_of_unum
    l1.sort()
    l2.sort()
    return l1 == l2


def play(difficulty):
    list_of_num = generate_sequence(difficulty)
    print(list_of_num)
    sleep(0.7)
    cmd = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(cmd, shell=True, check=False)
    list_of_unum = get_list_from_user(difficulty)
    return is_list_equal(list_of_num, list_of_unum)