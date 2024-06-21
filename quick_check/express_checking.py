from random import random


BANK = 1_000_000
SIM_TIMES = 1_000_000
SUPER = 0.05
BET_VALUE = 1
EXPRESS_SIZE = 1
PROB_DIFF = -0.1

bank = BANK
wins = []


def get_prob():
    return (random() + random() + random()) / 3


for _ in range(SIM_TIMES):
    bank -= BET_VALUE
    k = 1
    for _ in range(EXPRESS_SIZE):
        prob = get_prob() + PROB_DIFF
        if random() < prob * (1 + SUPER):
            k *= 1 / prob
        else:
            k = 0
            break
    bank += BET_VALUE * k
    if k > 0:
        wins.append(k)


print(f'start = {BANK:.2f}, result = {bank:.2f}, percent={bank/BANK*100:.2f}%')
print(f'avg_k = {sum(wins)/len(wins):.2f}')
