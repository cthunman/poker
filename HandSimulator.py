from models import Hand, Card, PLOStartingHand
import random
import itertools
from cards import cards
from collections import OrderedDict
from ComboUtils import *


class PLOHandSimulator():
    def __init__(self, handList, numPlayers, flop=None, turn=None, debug=True):
        self.handList = handList
        self.numPlayers = numPlayers
        self.debug = debug

    def simulate(self, runs):
        cardList = []
        cardDict = OrderedDict()
        for card in cards:
            c = Card(card)
            cardDict[card] = c

        for hand in self.handList:
            print(hand)
            for card in hand.cardList:
                print(card)
            for card in hand.cardList:
                del cardDict[str(card)]

        for card in cardDict:
            cardList.append(cardDict[card])

        handStats = {}
        for hand in self.handList:
            handStats[hand] = {
                'wins': 0,
                'handsPlayed': 0,
            }
        handHistory = {}

        for r in range(runs):
            handHistory[r] = {}
            if self.debug:
                print('run ' + str(r))
            idx = 0
            random.shuffle(cardList)
            handDict = {}
            # deal cards
            for i in range(len(self.handList)):
                if i not in handDict:
                    handDict[i] = {}
                handDict[i]['hand'] = self.handList[i]
            for i in range(len(self.handList), self.numPlayers):
                if i not in handDict:
                    handDict[i] = {}
                cardArgs = []
                for j in range(4):

                    cardArgs.append(str(cardList[idx]))
                    idx += 1

                handDict[i]['hand'] = PLOStartingHand(
                    [cardArgs[0], cardArgs[1], cardArgs[2], cardArgs[3]]
                )

            if self.debug:
                for h in handDict:
                    hand = ''
                    for c in handDict[h]['hand'].cardList:
                        hand += str(c) + ' '
                    print(h, hand)
            # deal board
            sharedCards = []
            for k in range(5):
                sharedCards.append(cardList[idx])
                idx += 1
            if self.debug:
                hand = ''
                for c in sharedCards:
                    hand += str(c) + ' '
                print('board ' + str(hand))
            madeHandDict = {}
            player_hands = []
            for player in handDict:
                best_hand = find_best_plo_hand(
                    handDict[player]['hand'].cardList, sharedCards)
                print(r, player)
                handHistory[r][player] = {
                    'hand': best_hand
                }
                player_hands.append(best_hand)
                madeHandDict[player] = best_hand

            if self.debug:
                print('winner')
                for w in find_winner_seat(madeHandDict):
                    print('\t' + str(w[0]) + ' : ' + str(w[1]))
                    handHistory[r]['winner'] = w[0]
                    handHistory[r]['winningHand'] = w[1]

        for h in handHistory:
            print(h, handHistory[h])


def main():
    hand1 = PLOStartingHand(['AS', 'KD', 'KC', 'AC'])
    # hand2 = PLOStartingHand('AD', 'KS', 'KH', 'AH')

    # s = PLOHandSimulator([hand1, hand2], 9, debug=True)
    s = PLOHandSimulator([hand1], 9, debug=True)
    s.simulate(2)

if __name__ == '__main__':
    main()
