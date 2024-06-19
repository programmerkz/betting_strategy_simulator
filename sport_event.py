from typing import Optional
import os
import random


FC_NAMES_FILE_NAME = os.path.join('.', 'english_football_clubs.txt')
NORM_RANDOM_N = 3
NORM_RANDOM_PREC = 4


class SportEvent:
    title: str
    prob: float
    _fc: Optional[list[str]] = None

    def __init__(self, title: Optional[str] = None, prob: Optional[float] = None) -> None:
        self.title = title if title else self._generate_random_title()
        self.prob = prob if prob else self._generate_normal_prob()

        assert len(self.title) > 3
        assert 0 <= self.prob <= 1

    def __repr__(self) -> str:
        return '{0} [{1:.{3}f} {2:.{3}f}]'.format(self.title, self.prob, 1 - self.prob, NORM_RANDOM_PREC)

    def _generate_normal_prob(self) -> float:
        probs = [random.random() for _ in range(NORM_RANDOM_N)]

        return sum(probs) / NORM_RANDOM_N

    def _generate_random_title(self) -> str:
        if not SportEvent._fc:
            SportEvent._fc = self._get_fc_names()
            assert len(SportEvent._fc) > 1

        n = len(SportEvent._fc) - 1
        id_1 = random.randint(0, n - 1)
        id_2 = random.randint(0, n - 1)

        while id_1 == id_2:
            id_2 = random.randint(0, n - 1)

        return ' - '.join([SportEvent._fc[id_1], SportEvent._fc[id_2]])

    def _get_fc_names(self) -> list[str]:
        with open(FC_NAMES_FILE_NAME, 'r') as f:
            cont = f.read()
            fc_names: list[str] = []

            for line in cont.splitlines():
                fc_names.append(line)

        return fc_names
