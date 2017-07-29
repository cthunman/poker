from models import Hand, Card
import random
import itertools
from cards import cards


def select_combinations(combo_list):
    combos = []
    for combo in combo_list:
        combos.append(itertools.combinations(combo[0], combo[1]))

    combined_results = itertools.product(*combos)
    result_list = []
    for r in combined_results:
        result_list.append([i for sub in r for i in sub])

    return result_list


def find_best_hand(cardlist):
    combos = itertools.combinations(cardlist, 5)
    best_hand = None
    for c in combos:
        if best_hand is None:
            best_hand = Hand(c)
        else:
            compare = best_hand.compare_to_hand(Hand(c))
            if compare == 1:
                continue
            elif compare == -1:
                best_hand = Hand(c)
            elif compare == 0:
                continue
    return best_hand


def find_winner(handlist):
    winner_list = [handlist[0]]
    for i in range(1, len(handlist)):
        if winner_list[0][1].compare_to_hand(handlist[i][1]) > 0:
            continue
        elif winner_list[0][1].compare_to_hand(handlist[i][1]) < 0:
            winner_list = [handlist[i]]
        elif winner_list[0][1].compare_to_hand(handlist[i][1]) == 0:
            winner_list.append(handlist[i])
    return winner_list


def find_winner_seat(handDict):
    winner_list = []
    current_best = None
    for h in handDict:
        if len(winner_list) == 0:
            winner_list.append((h, handDict[h]))
            current_best = handDict[h]
        elif current_best.compare_to_hand(handDict[h]) > 0:
            continue
        elif current_best.compare_to_hand(handDict[h]) < 0:
            winner_list = [(h, handDict[h])]
        elif current_best.compare_to_hand(handDict[h]) == 0:
            winner_list.append((h, handDict[h]))
    return winner_list


# I think this should work for Big O also
def find_best_plo_hand(player_cards, shared_cards):
    combos = select_combinations([
        (player_cards, 2),
        (shared_cards, 3),
    ])
    best_hand = None
    for c in combos:
        if best_hand is None:
            best_hand = Hand(list(c))
        else:
            compare = best_hand.compare_to_hand(Hand(list(c)))
            if compare == 1:
                continue
            elif compare == -1:
                best_hand = Hand(list(c))
            elif compare == 0:
                continue
    return best_hand


def test_nlh(num_players=4, debug=False, file=None):
    # f = open('db.txt', 'wb+')
    hand_record = {}
    cardlist = []
    for card in cards:
        cardlist.append(Card(card))
    random.shuffle(cardlist)

    playerlist = []
    for p in range(num_players):
        playerlist.append({'cards': []})

    hand_record['starting_hands'] = {}
    for index, player in enumerate(playerlist):
        player['cards'].append(cardlist.pop())
        player['cards'].append(cardlist.pop())
        hand_record['starting_hands'][index + 1] = []
        for c in player['cards']:
            hand_record['starting_hands'][index + 1].append(str(c))
        if file is not None:
            file.write('player' + str(index + 1) + ': ')
            for c in player['cards']:
                file.write(str(c) + ' ')
            file.write('\n')

    shared_cards = []
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    hand_record['shared_cards'] = []
    for c in shared_cards:
        hand_record['shared_cards'].append(str(c))
    hand_record['flop'] = []
    for c in shared_cards[0:3]:
        hand_record['flop'].append(str(c))
    hand_record['turn'] = str(shared_cards[3])
    hand_record['river'] = str(shared_cards[4])

    if file is not None:
        file.write('shared cards: ')
        for c in shared_cards:
            file.write(str(c) + ' ')
        file.write('\n')

    for index, player in enumerate(playerlist):
        card_string = ''
        for card in player['cards']:
            card_string += str(card) + ' '
        if debug:
            print('Player' + str(index + 1) + ': ' + str(card_string))
        index += 1
    card_string = ''
    for card in shared_cards:
        card_string += str(card) + ' '
    if debug:
        print('Shared cards: ' + card_string)

    player_hands = []
    for index, player in enumerate(playerlist):
        card_set = []
        card_set.extend(player['cards'])
        card_set.extend(shared_cards)

        card_string = ''
        for card in card_set:
            card_string += str(card) + ' '
        if debug:
            print('Player' + str(index + 1) + ': ' + str(card_string))
        best_hand = find_best_hand(card_set)
        player_hands.append(best_hand)
        if debug:
            print(str(best_hand))

        combos = itertools.combinations(card_set, 5)
        for combo in combos:
            card_string = ''
            for c in combo:
                card_string += str(c) + ' '
    hand_record['player_hands'] = {}
    for index, h in enumerate(player_hands):
        hand_record['player_hands'][index + 1] = str(h)
        file.write('player ' + str(index + 1) + ': ' + str(h) + ' \n')

    winner = find_winner(player_hands)
    hand_record['winner'] = {}
    hand_record['winner']['hand'] = []
    if len(winner) > 1:
        file.write('SPLIT POT: ')
        hand_record['winner']['status'] = 'SPLIT POT'
        for w in winner:
            file.write(str(w) + ' ')
            hand_record['winner']['hand'].append(str(w))
    else:
        file.write('WINNER: ')
        hand_record['winner']['status'] = 'WINNER'
        hand_record['winner']['hand'].append(str(winner[0]))
        file.write(str(winner[0]))
    file.write('\n\n')
    file.write(str(hand_record))
    file.write('\n\n')

    return find_winner(player_hands), player_hands


def test_plo(num_players=4, debug=False):
    cardlist = []
    for card in cards:
        cardlist.append(Card(card))
    random.shuffle(cardlist)

    playerlist = []
    for p in range(num_players):
        playerlist.append({'cards': []})

    for player in playerlist:
        player['cards'].append(cardlist.pop())
        player['cards'].append(cardlist.pop())
        player['cards'].append(cardlist.pop())
        player['cards'].append(cardlist.pop())

    shared_cards = []
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())

    for index, player in enumerate(playerlist):
        card_string = ''
        for card in player['cards']:
            card_string += str(card) + ' '
        if debug:
            print('Player' + str(index + 1) + ': ' + str(card_string))
        index += 1
    card_string = ''
    for card in shared_cards:
        card_string += str(card) + ' '
    if debug:
        print('Shared cards: ' + card_string)

    player_hands = []
    for index, player in enumerate(playerlist):
        card_set = []
        card_set.extend(player['cards'])
        card_set.extend(shared_cards)

        card_string = ''
        for card in card_set:
            card_string += str(card) + ' '
        if debug:
            print('Player' + str(index + 1) + ': ' + str(card_string))
        best_hand = find_best_plo_hand(player['cards'], shared_cards)
        player_hands.append(best_hand)
        if debug:
            print(str(best_hand))

        combos = itertools.combinations(card_set, 5)
        for combo in combos:
            card_string = ''
            for c in combo:
                card_string += str(c) + ' '

    if debug:
        print('find_winner(player_hands)')
    for h in find_winner(player_hands):
        if debug:
            print(str(h))
    return find_winner(player_hands), player_hands


def test_big_o(num_players=4, debug=False):
    cardlist = []
    for card in cards:
        cardlist.append(Card(card))
    random.shuffle(cardlist)

    playerlist = []
    for p in range(num_players):
        playerlist.append({'cards': []})

    for player in playerlist:
        player['cards'].append(cardlist.pop())
        player['cards'].append(cardlist.pop())
        player['cards'].append(cardlist.pop())
        player['cards'].append(cardlist.pop())
        player['cards'].append(cardlist.pop())

    shared_cards = []
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())
    shared_cards.append(cardlist.pop())

    for index, player in enumerate(playerlist):
        card_string = ''
        for card in player['cards']:
            card_string += str(card) + ' '
        if debug:
            print('Player' + str(index + 1) + ': ' + str(card_string))
        index += 1
    card_string = ''
    for card in shared_cards:
        card_string += str(card) + ' '
    if debug:
        print('Shared cards: ' + card_string)

    player_hands = []
    for index, player in enumerate(playerlist):
        card_set = []
        card_set.extend(player['cards'])
        card_set.extend(shared_cards)

        card_string = ''
        for card in card_set:
            card_string += str(card) + ' '
        if debug:
            print('Player' + str(index + 1) + ': ' + str(card_string))
        best_hand = find_best_plo_hand(player['cards'], shared_cards)
        player_hands.append(best_hand)
        if debug:
            print(str(best_hand))

        combos = itertools.combinations(card_set, 5)
        for combo in combos:
            card_string = ''
            for c in combo:
                card_string += str(c) + ' '

    if debug:
        print('find_winner(player_hands)')
    for h in find_winner(player_hands):
        if debug:
            print(str(h))
    return find_winner(player_hands), player_hands
