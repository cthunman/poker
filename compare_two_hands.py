from Hand import Hand, Card
import random
import copy
import itertools
import ComboUtils as cu
from cards import cards


def main():
    # card1 = Card('AS')
    # card2 = Card('AC')
    # card3 = Card('KC')
    # card4 = Card('KS')

    # card5 = Card('7H')
    # card6 = Card('8H')
    # card7 = Card('9D')
    # card8 = Card('TD')

    card_list = copy.copy(cards)
    # print(card_list)
    deck = []
    for c in card_list:
        deck.append(Card(c))

    card1 = deck.pop(card_list.index('AS'))
    card_list.remove('AS')
    card2 = deck.pop(card_list.index('AC'))
    card_list.remove('AC')
    card3 = deck.pop(card_list.index('KC'))
    card_list.remove('KC')
    card4 = deck.pop(card_list.index('KS'))
    card_list.remove('KS')

    card5 = deck.pop(card_list.index('7H'))
    card_list.remove('7H')
    card6 = deck.pop(card_list.index('8H'))
    card_list.remove('8H')
    card7 = deck.pop(card_list.index('9D'))
    card_list.remove('9D')
    card8 = deck.pop(card_list.index('TD'))
    card_list.remove('TD')

    player1_cards = [card1, card2, card3, card4]
    player2_cards = [card5, card6, card7, card8]

    for i in range(5):
        print('--------------------------------------')
        random.shuffle(deck)
        board_cards = [deck[0], deck[1], deck[2], deck[3], deck[4]]

        flop = [deck[0], deck[1], deck[2]]
        turn = deck[3]
        river = deck[4]
        flop_str = str(flop[0]) + ', ' + str(flop[1]) + ', ' + str(flop[2])
        # print('flop:\t' + flop_str)
        # print('turn:\t' + str(turn))
        # print('river:\t' + str(river))
        print('board:\t' + flop_str + ', ' + str(turn) + ', ' + str(river))
        player1_hand = cu.find_best_plo_hand(player1_cards, board_cards)
        print('player 1: ' + str(player1_hand))
        player2_hand = cu.find_best_plo_hand(player2_cards, board_cards)
        print('player 2: ' + str(player2_hand))
        print('\tWinning hand:')
        for hand in cu.find_winner([player1_hand, player2_hand]):
            print('\t' + str(hand))
        print('--------------------------------------')
        print('\n\n')


if __name__ == '__main__':
    main()
