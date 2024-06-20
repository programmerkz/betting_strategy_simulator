def calc_margin(bk_odds: list[float]) -> float:
    total = sum(1 / bk_odd for bk_odd in bk_odds)

    return total - 1


if __name__ == '__main__':
    # import contants from settings
    import os
    import sys

    sys.path.append(os.getcwd())
    from settings_bss.conts import SPORT_BET_ODDS_PREC

    try:
        args = [float(arg) for arg in sys.argv[1:]]

        print('margin = {0:.{1}f}'.format(calc_margin(args), SPORT_BET_ODDS_PREC))
    except TypeError as err:
        print(err)
