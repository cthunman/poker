from Hand import Hand, Card
import random, itertools

cards = [
	'2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS','AS',
	'2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC','AC',
	'2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AH',
	'2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD','AD',
]

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

def test_nlh():
	cardlist = []
	for card in cards:
		cardlist.append(Card(card))
	random.shuffle(cardlist)
	
	playerlist = []
	playerlist.append({'cards':[]})
	playerlist.append({'cards':[]})
	playerlist.append({'cards':[]})
	playerlist.append({'cards':[]})

	for player in playerlist:
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
			card_string += unicode(card) + ' '
		print 'Player' + unicode(index + 1) + ': ' + unicode(card_string)
		index += 1
	card_string = ''
	for card in shared_cards:
		card_string += unicode(card) + ' '
	print 'Shared cards: ' + card_string

	for index, player in enumerate(playerlist):
		card_set = []
		card_set.extend(player['cards'])
		card_set.extend(shared_cards)
		
		card_string = ''
		for card in card_set:
			card_string += unicode(card) + ' '
		print 'Player' + unicode(index + 1) + ': ' + unicode(card_string)
		best_hand = find_best_hand(card_set)
		print unicode(best_hand)

		combos = itertools.combinations(card_set, 5)
		for combo in combos:
			card_string = ''
			for c in combo:
				card_string += unicode(c) + ' '

def test_plo():
	cardlist = []
	for card in cards:
		cardlist.append(Card(card))
	random.shuffle(cardlist)
	
	playerlist = []
	playerlist.append({'cards':[]})
	playerlist.append({'cards':[]})
	playerlist.append({'cards':[]})
	playerlist.append({'cards':[]})

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
			card_string += unicode(card) + ' '
		print 'Player' + unicode(index + 1) + ': ' + unicode(card_string)
		index += 1
	card_string = ''
	for card in shared_cards:
		card_string += unicode(card) + ' '
	print 'Shared cards: ' + card_string

	for index, player in enumerate(playerlist):
		card_set = []
		card_set.extend(player['cards'])
		card_set.extend(shared_cards)
		
		card_string = ''
		for card in card_set:
			card_string += unicode(card) + ' '
		print 'Player' + unicode(index + 1) + ': ' + unicode(card_string)
		best_hand = find_best_plo_hand(player['cards'], shared_cards)
		print unicode(best_hand)

		combos = itertools.combinations(card_set, 5)
		for combo in combos:
			card_string = ''
			for c in combo:
				card_string += unicode(c) + ' '

def main():
	test_plo()

if __name__ == '__main__':
	main()
