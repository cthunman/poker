from models import Card
from copy import copy
import itertools


# def calculate_nuts_plo(board_cards):
#     possible_hands = set(['set', 'pair'])
#     values = []
#     suits = {}
#     for card in board_cards:
#         values.append(card.numeric_value)

#     values = sorted(values)
#     i = 0
#     while i < len(values) - 2:
#         diff1 = values[i + 1] - values[i]
#         diff2 = values[i + 2] - values[i + 1]
#         if (diff1 > 0 and diff2 > 0 and
#                 diff1 + diff2 < 5 and diff1 + diff2 > 1):
#             possible_hands.add('straight')
#             break
#         elif diff1 == 0 or diff2 == 0:
#             possible_hands.add('quads')
#             possible_hands.add('full house')
#         i += 1
#     return possible_hands


def find_straights_plo(board_cards):
    possible_straights = {}

    values = []
    if type(board_cards[0]) == int:
        values = sorted(board_cards, reverse=True)
    else:
        for card in board_cards:
            values.append(card.numeric_value)
            if card.numeric_value == 14:
                values.append(1)
        values = sorted(values, reverse=True)

    for i0 in range(14, 4, -1):
        i1 = i0 - 1
        i2 = i0 - 2
        i3 = i0 - 3
        i4 = i0 - 4
        current_range = frozenset([i0, i1, i2, i3, i4])

        target_range = set()
        for i in current_range:
            if i in values:
                target_range.add(i)

        diff = current_range - target_range
        if len(diff) == 2:
            possible_straights[i0] = set()
            possible_straights[i0].add(frozenset(diff))
        elif len(diff) == 1:
            possible_straights[i0] = set()
            for card in target_range:
                new_diff = set(diff)
                new_diff.add(card)
                possible_straights[i0].add(frozenset(new_diff))
        elif len(diff) == 0:
            possible_straights[i0] = set()
            for combo in itertools.combinations(current_range, 2):
                possible_straights[i0].add(frozenset(combo))

    return possible_straights


def find_straight_outs_plo(board_cards, player_hand):
    value_count = {
        'A': 4,
        13: 4,
        12: 4,
        11: 4,
        10: 4,
        9: 4,
        8: 4,
        7: 4,
        6: 4,
        5: 4,
        4: 4,
        3: 4,
        2: 4,
    }
    outs = {}
    board_values = []
    for card in board_cards:
        board_values.append(card.numeric_value)
        if card.numeric_value == 14:
            board_values.append(1)
            value_count['A'] -= 1
        else:
            value_count[card.numeric_value] -= 1
    board_values = sorted(board_values, reverse=True)

    player_values = []
    for card in player_hand:
        player_values.append(card.numeric_value)
        if card.numeric_value == 14:
            player_values.append(1)
            value_count['A'] -= 1
        else:
            value_count[card.numeric_value] -= 1

    player_values = sorted(player_values, reverse=True)
    player_combos = set()

    for combo in itertools.combinations(player_values, 2):
        player_combos.add(frozenset(combo))

    for i in range(14, 0, -1):
        if i == 14 or i == 1:
            num_outs = value_count['A']
        else:
            num_outs = value_count[i]
        if i in board_values:
            continue
        test_board_values = copy(board_values)
        test_board_values.append(i)
        possible_straights = find_straights_plo(test_board_values)

        if len(possible_straights) > 0:
            nuts = sorted(possible_straights.keys(), reverse=True)[0]
        for straight in possible_straights:
            made_hands = possible_straights[straight]
            if len(made_hands.intersection(player_combos)) > 0:
                if i in outs:
                    if straight < outs[i][0]:
                        continue
                outs[i] = (straight, nuts, num_outs)

    return outs


def format_outs(outs):
    output = {}
    output['nut_outs'] = {'count': 0, 'cards': set()}
    output['non_nut_outs'] = {'count': 0, 'cards': set()}
    for out, item in outs.items():
        if item[0] == item[1]:
            output['nut_outs']['count'] += item[2]
            output['nut_outs']['cards'].add(out)
        else:
            output['non_nut_outs']['count'] += item[2]
            output['non_nut_outs']['cards'].add(out)
    return output


def main():
    card1 = Card('AS')
    card2 = Card('2S')
    card3 = Card('3C')

    card4 = Card('AD')
    card5 = Card('2D')
    card6 = Card('5C')
    card7 = Card('JC')

    outs = find_straight_outs_plo(
               [card1, card2, card3],
               [card4, card5, card6, card7]
           )
    print(str(card1), str(card2), str(card3))
    print(str(card4), str(card5), str(card6), str(card7))
    print(format_outs(outs))
    print('\n\n')

    card1 = Card('3S')
    card2 = Card('TS')
    card3 = Card('JC')

    card4 = Card('9D')
    card5 = Card('8D')
    card6 = Card('QC')
    card7 = Card('KC')

    outs = find_straight_outs_plo(
               [card1, card2, card3],
               [card4, card5, card6, card7]
           )
    print(str(card1), str(card2), str(card3))
    print(str(card4), str(card5), str(card6), str(card7))
    print(format_outs(outs))
    print('\n\n')

    card1 = Card('3S')
    card2 = Card('TS')
    card3 = Card('JC')

    card4 = Card('9D')
    card5 = Card('8D')
    card6 = Card('TC')
    card7 = Card('JC')

    outs = find_straight_outs_plo(
               [card1, card2, card3],
               [card4, card5, card6, card7]
           )
    print(str(card1), str(card2), str(card3))
    print(str(card4), str(card5), str(card6), str(card7))
    print(format_outs(outs))
    print('\n\n')

    card1 = Card('3S')
    card2 = Card('6S')
    card3 = Card('7C')

    card4 = Card('9D')
    card5 = Card('8D')
    card6 = Card('TC')
    card7 = Card('9C')

    outs = find_straight_outs_plo(
               [card1, card2, card3],
               [card4, card5, card6, card7]
           )
    print(str(card1), str(card2), str(card3))
    print(str(card4), str(card5), str(card6), str(card7))
    print(format_outs(outs))
    print('\n\n')

    card1 = Card('5S')
    card2 = Card('6S')
    card3 = Card('7C')

    print(find_straights_plo([card1, card2, card3]))

if __name__ == '__main__':
    main()
