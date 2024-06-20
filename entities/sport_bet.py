from entities.sport_event import SportEvent
from settings_bss.conts import SPORT_BET_MARGIN_PREC, SPORT_BET_ODDS_PREC


class SportBet:
    def __init__(self, sport_event: SportEvent, margin: float) -> None:
        assert sport_event, 'Sport event must be not None'
        assert 0 <= margin <= 1, 'Margin must be positive and less than 1.0'

        self.sport_event = sport_event
        self.margin = margin

        self._calculate_odds()

    def _calculate_odds(self) -> None:
        margin_1 = self.margin * self.sport_event.prob
        margin_2 = self.margin * (1 - self.sport_event.prob)

        self.odd_1 = 1 / (self.sport_event.prob + margin_1)
        self.odd_2 = 1 / (1 - self.sport_event.prob + margin_2)

    def __repr__(self) -> str:
        return '{0}, bk_margin={1:.{4}f}, odds: {2:.{5}f} {3:.{5}f}'.format(
            self.sport_event,
            self.margin,
            self.odd_1,
            self.odd_2,
            SPORT_BET_MARGIN_PREC,
            SPORT_BET_ODDS_PREC,
        )
