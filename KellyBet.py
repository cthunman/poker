from decimal import Decimal


# odds = b where bet pays out (b to 1)
def kellyFraction(winProbability, odds):
    # assert(type(winProbability) == type(Decimal))
    # assert(type(odds) == type(Decimal))

    return max(((winProbability * (odds + 1)) - 1) / odds, 0)


def kellyCall(betAmount, potSize, winProbability, bankroll):
    # assert(type(betAmount) == type(Decimal))
    # assert(type(potSize) == type(Decimal))
    # assert(type(winProbability) == type(Decimal))
    # assert(type(bankroll) == type(Decimal))

    f = Decimal(betAmount) / Decimal(bankroll)
    odds = (potSize + betAmount) / betAmount
    payout = ((winProbability * (odds + 1)) - 1) / odds

    return payout / f > 1


def kellyRaisePot(betAmount, potSize, winProbability, bankroll):

    totalBet = (potSize + (betAmount * 2)) * 2
    f = Decimal(totalBet) / Decimal(bankroll)
    odds = 2
    payout = ((winProbability * (odds + 1)) - 1) / odds
    return (payout / f) > 1


def kellyAction(betAmount, potSize, winProbability, bankroll):
    if kellyRaisePot(betAmount, potSize, winProbability, bankroll):
        return 'RAISE'
    elif kellyCall(betAmount, potSize, winProbability, bankroll):
        return 'CALL'
    else:
        return 'FOLD'


def main():

    actions = {
        'RAISE': '^^^^',
        'CALL': 'OOOO',
        'FOLD': '____'
    }

    bankroll = Decimal(950)
    topRow = '\t'
    increment = Decimal('.05')
    for i in range(20):
        topRow += str(((i + 1) * increment) * 100) + '%\t'
    print(topRow)
    for b in range(2, 60, 2):
        row = ''
        row += str((b)) + '\t'
        for i in range(1, 21):
            bet = (b)
            winProbability = ((i) * increment)
            row += str(actions[kellyAction(
                       betAmount=bet,
                       potSize=bet,
                       winProbability=winProbability,
                       bankroll=bankroll)]) + '\t'
        print(row)

    for b in range(6, 21):
        row = ''
        row += str((b) * 10) + '\t'
        for i in range(1, 21):
            bet = ((b) * 10)
            winProbability = ((i) * increment)
            row += str(actions[kellyAction(
                       betAmount=bet,
                       potSize=bet,
                       winProbability=winProbability,
                       bankroll=bankroll)]) + '\t'
        print(row)


if __name__ == '__main__':
    main()
