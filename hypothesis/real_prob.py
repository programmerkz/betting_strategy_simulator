import random
from entities.sport_event import SportEvent
from settings_bss.conts import HYPOTHESIS_CHECK_N_TIMES


class RealProbHypothesis:
    '''Real Probability Hypothesis

    Simulate N times to check real probability

    '''

    def __init__(self, sport_event: SportEvent = None) -> None:
        self.se = sport_event if sport_event else SportEvent()

    def simulate(self):
        left, right = 0, 0
        for _ in range(HYPOTHESIS_CHECK_N_TIMES):
            if random.random() > self.se.prob:
                right += 1
            else:
                left += 1

        print('Sport event: ', self.se)
        print(f'Results after {HYPOTHESIS_CHECK_N_TIMES} simulations:')
        print('Distribution: ', left / HYPOTHESIS_CHECK_N_TIMES, right / HYPOTHESIS_CHECK_N_TIMES)
