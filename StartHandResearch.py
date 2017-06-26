from Hand import Hand, Card
import random
import itertools
from cards import cards


class NLStartHand():

    def sort_cards(self, card_list):
        # suit order: spades, clubs, hearts, diamonds
        # descending numerical order
        return sorted(
            card_list, key=lambda card: card.numeric_value, reverse=True)

    def hand_key(self):
        suited = self.card1.suit == self.card2.suit
        suit = ''
        if suited:
            suit = 's'
        else:
            suit = 'o'
        return str(self.card1.value) + str(self.card2.value) + str(suit)

    def __init__(self, card_list):
        sorted_cards = self.sort_cards(card_list)
        self.card1 = sorted_cards[0]
        self.card2 = sorted_cards[1]


def test_starting_hand(starting_hand, num_opponents, runs=1000, debug=False):
    cardlist = []
    for card in cards:
        c = Card(card)
        if c.equals_card(starting_hand.card1):
            continue
        if c.equals_card(starting_hand.card2):
            continue
        cardlist.append(Card(card))

    for i in range(runs):

        temp_cardlist = list(cardlist)
        random.shuffle(temp_cardlist)

        playerlist = []
        playerlist.append({'cards': []})

        for p in range(num_opponents):
            playerlist.append({'cards': []})

        for player in playerlist:
            player['cards'].append(temp_cardlist.pop())
            player['cards'].append(temp_cardlist.pop())

        shared_cards = []
        shared_cards.append(temp_cardlist.pop())
        shared_cards.append(temp_cardlist.pop())
        shared_cards.append(temp_cardlist.pop())
        shared_cards.append(temp_cardlist.pop())
        shared_cards.append(temp_cardlist.pop())

        for index, player in enumerate(playerlist):
            card_string = ''
            for card in player['cards']:
                card_string += str(card) + ' '
            if debug:
                print 'Player' + str(index + 1) + ': ' + str(card_string)
            index += 1
        card_string = ''
        for card in shared_cards:
            card_string += str(card) + ' '
        if debug:
            print 'Shared cards: ' + card_string

        player_hands = []
        for index, player in enumerate(playerlist):
            card_set = []
            card_set.extend(player['cards'])
            card_set.extend(shared_cards)

            card_string = ''
            for card in card_set:
                card_string += str(card) + ' '
            if debug:
                print 'Player' + str(index + 1) + ': ' + str(card_string)
            best_hand = find_best_hand(card_set)
            player_hands.append(best_hand)
            if debug:
                print str(best_hand)

            combos = itertools.combinations(card_set, 5)
            for combo in combos:
                card_string = ''
                for c in combo:
                    card_string += str(c) + ' '
        return find_winner(player_hands), player_hands


def main():
    cardlist = []
    for card in cards:
        cardlist.append(Card(card))
    random.shuffle(cardlist)

    hand = NLStartHand([cardlist.pop(), cardlist.pop()])
    print hand.hand_key()
    print len(test_starting_hand(hand, 5))
    shuffled_cards = test_starting_hand(hand, 5)


if __name__ == '__main__':
    main()
