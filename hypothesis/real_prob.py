import random
from entities.sport_event import SportEvent


N_TIMES = 10**6


class RealProbHypothesis:
    '''Real Probability Hypothesis

    Simulate N times to check real probability

    '''

    def __init__(self, sport_event: SportEvent = None) -> None:
        self.se = sport_event if sport_event else SportEvent()

    def simulate(self):
        left, right = 0, 0
        for _ in range(N_TIMES):
            if random.random() > self.se.prob:
                right += 1
            else:
                left += 1

        print('Sport event: ', self.se)
        print(f'Results after {N_TIMES} simulations:')
        print('Distribution: ', left / N_TIMES, right / N_TIMES)
