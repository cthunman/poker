import sys
import json
from datetime import datetime
from models import Hand, Card, PLOStartingHand
import random
import copy
import itertools
import ComboUtils as cu
from cards import cards

from pymongo import MongoClient


def main():
    if len(sys.argv) != 6:
        print('Enter your cards, bruh.')


    card_list = copy.copy(cards)

    deck = []
    for c in card_list:
        deck.append(Card(c))

    c1 = sys.argv[1]
    c2 = sys.argv[2]
    c3 = sys.argv[3]
    c4 = sys.argv[4]
    num_opponents = sys.argv[5]

    card1 = deck.pop(card_list.index(c1))
    card_list.remove(c1)
    card2 = deck.pop(card_list.index(c2))
    card_list.remove(c2)
    card3 = deck.pop(card_list.index(c3))
    card_list.remove(c3)
    card4 = deck.pop(card_list.index(c4))
    card_list.remove(c4)

    hero_cards = [card1, card2, card3, card4]
    hero_plo_hand = PLOStartingHand(hero_cards)
    results = []

    winner_totals = {}
    runs = 10000

    for i in range(runs):
        random.shuffle(deck)
        board_cards = [deck[0], deck[1], deck[2], deck[3], deck[4]]
        result = {}
        result['hero_suit_id'] = hero_plo_hand.suit_id()

        d_idx = 0
        for j in range(num_opponents):
            for k in range(4):
                opponent_cards = [deck[d_idx],
                    deck[d_idx + 1], deck[d_idx + 2], deck[d_idx + 3]]

# TODO

            result['opponent_hand'] = player_2_plo_hand.value_id()
            result['opponent_suit_id'] = player_2_plo_hand.suit_id()

        flop = [deck[0], deck[1], deck[2]]
        turn = deck[3]
        river = deck[4]
        result['flop'] = [str(c) for c in flop]
        result['turn'] = str(turn)
        result['river'] = str(river)

        flop_str = str(flop[0]) + ', ' + str(flop[1]) + ', ' + str(flop[2])
        hero_hand = cu.find_best_plo_hand(hero_cards, board_cards)
        result['hero_hand'] = str(hero_hand)

        player_2_hand = cu.find_best_plo_hand(player_2_cards, board_cards)
        result['player_2_hand'] = str(player_2_hand)

        result['winner'] = []
        result['winning_players'] = []
        for hand in cu.find_winner([(1, hero_hand), (2, player_2_hand)]):
            result['winner'].append(
                (hand[0], str(hand[1]), str(hand[1].value)))
            result['winning_players'].append(hand[0])
            if hand[0] not in winner_totals:
                winner_totals[hand[0]] = 0
            winner_totals[hand[0]] += 1

        results.append(result)

    c = MongoClient()
    db = c.plo
    collection = db[hero_plo_hand.value_id()]
    collection.insert_many(results)

if __name__ == '__main__':
    main()

