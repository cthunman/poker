import sys
import json
from datetime import datetime
from models import Hand, Card
import random
import copy
import itertools
import ComboUtils as cu
from cards import cards


def main():
    if len(sys.argv) != 9:
        print('Enter your cards, bruh.')

    card_list = copy.copy(cards)

    deck = []
    for c in card_list:
        deck.append(Card(c))

    c1 = sys.argv[1]
    c2 = sys.argv[2]
    c3 = sys.argv[3]
    c4 = sys.argv[4]
    c5 = sys.argv[5]
    c6 = sys.argv[6]
    c7 = sys.argv[7]
    c8 = sys.argv[8]

    card1 = deck.pop(card_list.index(c1))
    card_list.remove(c1)
    card2 = deck.pop(card_list.index(c2))
    card_list.remove(c2)
    card3 = deck.pop(card_list.index(c3))
    card_list.remove(c3)
    card4 = deck.pop(card_list.index(c4))
    card_list.remove(c4)

    card5 = deck.pop(card_list.index(c5))
    card_list.remove(c5)
    card6 = deck.pop(card_list.index(c6))
    card_list.remove(c6)
    card7 = deck.pop(card_list.index(c7))
    card_list.remove(c7)
    card8 = deck.pop(card_list.index(c8))
    card_list.remove(c8)

    player1_cards = [card1, card2, card3, card4]
    player2_cards = [card5, card6, card7, card8]

    results = []
    winner_totals = {}
    runs = 1000

    for i in range(runs):
        random.shuffle(deck)
        board_cards = [deck[0], deck[1], deck[2], deck[3], deck[4]]
        result = {}

        flop = [deck[0], deck[1], deck[2]]
        turn = deck[3]
        river = deck[4]
        result['flop'] = [str(c) for c in flop]
        result['turn'] = str(turn)
        result['river'] = str(river)

        flop_str = str(flop[0]) + ', ' + str(flop[1]) + ', ' + str(flop[2])
        player1_hand = cu.find_best_plo_hand(player1_cards, board_cards)
        result['player1_hand'] = str(player1_hand)

        player2_hand = cu.find_best_plo_hand(player2_cards, board_cards)
        result['player2_hand'] = str(player2_hand)

        result['winner'] = []
        for hand in cu.find_winner([(1, player1_hand), (2, player2_hand)]):
            result['winner'].append(
                (hand[0], str(hand[1]), str(hand[1].value)))
            if hand[0] not in winner_totals:
                winner_totals[hand[0]] = 0
            winner_totals[hand[0]] += 1

        results.append(result)

    filename = 'data/'
    for card in player1_cards:
        filename += str(card)
    filename += 'vs'
    for card in player2_cards:
        filename += str(card)
    filename += 'x'
    filename += str(runs)
    filename += '@'
    filename += datetime.now().strftime('%y%m%d_%H:%M:%S')
    filename += '.plo'

    with open(filename, 'w+') as f:
        f.write(str(winner_totals))
        f.write(str(results))

if __name__ == '__main__':
    main()
