def calc_real_odds(bk_odds: list[float]) -> list[float]:
    assert len(bk_odds) > 0, 'Bookmaker odds list must have more than 0 odd.'

    probs = [1 / bk_odd for bk_odd in bk_odds]
    prob_sum = sum(probs)
    print('prob_sum = ', prob_sum)
    return [prob_sum / prob for prob in probs]


if __name__ == '__main__':
    # import contants from settings
    import os
    import sys

    sys.path.append(os.getcwd())
    from tools.calc_margin import calc_margin
    from settings_bss.conts import SPORT_BET_ODDS_PREC, PLAYER_ADAVANTAGE

    try:
        args = [float(arg) for arg in sys.argv[1:]]
        r_odds = calc_real_odds(args)

        print('margin = {0:.{1}f}'.format(calc_margin(args), SPORT_BET_ODDS_PREC))
        print('real odds', ['{0:.{1}f}'.format(r_odd, SPORT_BET_ODDS_PREC) for r_odd in r_odds])

        # player supremence odds (%) = PLAYER_ADAVANTAGE
        s_odds = [r_odd * (1 + PLAYER_ADAVANTAGE) for r_odd in r_odds]
        print('super odds', ['{0:.{1}f}'.format(s_odd, SPORT_BET_ODDS_PREC) for s_odd in s_odds])

    except TypeError as err:
        print(err)
