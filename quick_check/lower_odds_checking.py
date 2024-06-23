from random import random


ODDS_DIFF = 0.07
PLAYER_ADV = 0.07

bank = 10**6

for _ in range(10**6):
    bank -= 1

    bet_prop: float = (random() + random() + random()) / 3

    if random() < bet_prop * (1 + PLAYER_ADV):
        bank += 1 / (bet_prop * (1 + ODDS_DIFF))


print(f'bank = {bank}, perc = {bank / 10**6 * 100:.4f}')
