import random
from entities.sport_event import SportEvent
from entities.sport_bet import SportBet
from settings_bss.conts import HYPOTHESIS_CHECK_N_TIMES


class BetTestHypothesis:
    def __init__(self, sport_event: SportEvent = None) -> None:
        if not sport_event:
            sport_event = SportEvent()

        self.sport_bet = SportBet(sport_event, 0.01)

    def simulate(self):
        bank = HYPOTHESIS_CHECK_N_TIMES

        for _ in range(HYPOTHESIS_CHECK_N_TIMES):
            bank -= 1

            if random.random() < self.sport_bet.sport_event.prob:
                bank += self.sport_bet.odd_1

        print('BetTestHypothesis')
        print('Sport bet: ', self.sport_bet)
        print(f'Results after {HYPOTHESIS_CHECK_N_TIMES} simulations:')
        print(f'bank = {bank}')
