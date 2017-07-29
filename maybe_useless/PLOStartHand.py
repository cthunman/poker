from Hand import Hand, Card
import random
import itertools
from cards import cards


class PLOStartHand():
    def __init__(self, *args):
        self.cardList = []
        for arg in args:
            self.cardList.append(Card(arg))

    def hand_decription(self):
        pass


def main():
    hand = PLOStartHand('AS', 'KD', '5D', 'AC')
    for card in hand.cardList:
        print str(card), str(card.value), str(card.suit)

if __name__ == '__main__':
    main()
