
# odds = b where bet pays out (b to 1)
def kellyFraction(winProbability, odds):
    return ((winProbability * (odds + 1)) - 1) / odds

def kellyCall(betAmount, potSize, winProbability, bankroll):

    f = float(betAmount) / float(bankroll)
    odds = (potSize + betAmount) / betAmount
    payout = ((winProbability * (odds + 1)) - 1) / odds

    return payout / f > 1

def kellyRaisePot(betAmount, potSize, winProbability, bankroll):

    totalBet = (potSize + (betAmount * 2)) * 2
    # print 'totalBet'
    # print totalBet
    f = float(totalBet) / float(bankroll)
    # print 'f'
    # print f
    odds = 2
    payout = ((winProbability * (odds + 1)) - 1) / odds
    # print 'payout'
    # print payout
    return (payout / f) > 1

def kellyAction(betAmount, potSize, winProbability, bankroll):
    if kellyRaisePot(betAmount, potSize, winProbability, bankroll):
        return 'RAISE'
    elif kellyCall(betAmount, potSize, winProbability, bankroll):
        return 'CALL'
    else:
        return 'FOLD'

def main():

    # print '---------'
    # print kellyCall(100.0, 100.0, .65, 700.0)
    # print unicode(700.0) + ' : ' + unicode(kellyRaisePot(100.0, 100.0, .65, 700.0))
    # print '---------'

    actions = {
        'RAISE' : '^^^^',
        'CALL' : 'OOOO',
        'FOLD' : '____'
    }

    bankroll = 1500
    topRow = '\t'
    for i in range(20):
        topRow += unicode(((i + 1) * .05) * 100) + '%\t'
    print topRow
    for b in range(2, 20, 2):
        row = ''
        row += unicode((b)) + '\t'
        for i in range(1, 20):
            bet = ((b))
            # print 'bet'
            # print bet
            winProbability = ((i) * .05)
            # print 'winProbability'
            # print winProbability
            row += unicode(actions[kellyAction(
                            betAmount=bet,
                            potSize=bet,
                            winProbability=winProbability,
                            bankroll=bankroll)]) + '\t'
        print row
    for b in range(2, 25):
        row = ''
        row += unicode((b) * 10) + '\t'
        for i in range(1, 20):
            bet = ((b) * 10)
            # print 'bet'
            # print bet
            winProbability = ((i) * .05)
            # print 'winProbability'
            # print winProbability
            row += unicode(actions[kellyAction(
                            betAmount=bet,
                            potSize=bet,
                            winProbability=winProbability,
                            bankroll=bankroll)]) + '\t'
        print row


if __name__ == '__main__':
    main()
