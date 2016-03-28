from Hand import Hand, Card
import random, itertools
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
		if winner_list[0].compare_to_hand(handlist[i]) > 0:
			continue
		elif winner_list[0].compare_to_hand(handlist[i]) < 0:
			winner_list = [handlist[i]]
		elif winner_list[0].compare_to_hand(handlist[i]) == 0:
			winner_list.append(handlist[i])
	return winner_list

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

def test_plo(num_players=4, debug=False):
	cardlist = []
	for card in cards:
		cardlist.append(Card(card))
	random.shuffle(cardlist)
	
	playerlist = []
	for p in range(num_players):
		playerlist.append({'cards':[]})
	# playerlist.append({'cards':[]})
	# playerlist.append({'cards':[]})
	# playerlist.append({'cards':[]})

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
		if debug:
			print 'Player' + unicode(index + 1) + ': ' + unicode(card_string)
		index += 1
	card_string = ''
	for card in shared_cards:
		card_string += unicode(card) + ' '
	if debug:
		print 'Shared cards: ' + card_string

	player_hands = []
	for index, player in enumerate(playerlist):
		card_set = []
		card_set.extend(player['cards'])
		card_set.extend(shared_cards)
		
		card_string = ''
		for card in card_set:
			card_string += unicode(card) + ' '
		if debug:
			print 'Player' + unicode(index + 1) + ': ' + unicode(card_string)
		best_hand = find_best_plo_hand(player['cards'], shared_cards)
		player_hands.append(best_hand)
		if debug:
			print unicode(best_hand)

		combos = itertools.combinations(card_set, 5)
		for combo in combos:
			card_string = ''
			for c in combo:
				card_string += unicode(c) + ' '

	if debug:
		print 'find_winner(player_hands)'
	# print unicode(find_winner(player_hands))
	for h in find_winner(player_hands):
		if debug:
			print unicode(h)
	return player_hands

def run_simulation(runs=1000, num_players=4, debug=False):
	winning_tally = {}
	winning_tally['straight_flush'] = 0
	winning_tally['quads'] = 0
	winning_tally['full_house'] = 0
	winning_tally['flush'] = 0
	winning_tally['straight'] = 0
	winning_tally['three_of_a_kind'] = 0
	winning_tally['two_pair'] = 0
	winning_tally['pair'] = 0
	winning_tally['high_card'] = 0
	for i in range(runs):
		if runs > 500 and i % 500 == 0: print i 
		winning_hands = test_plo(num_players=num_players)
		winning_tally[winning_hands[0].value] = winning_tally[winning_hands[0].value] + 1
		# for h in winning_hands:
		# 	if h.value not in winning_tally:
		# 		winning_tally[h.value] = 0
		# 	winning_tally[h.value] = winning_tally[h.value] + 1

	if debug:
		print 'straight_flush : ' + unicode(winning_tally['straight_flush'])
		print 'quads : ' + unicode(winning_tally['quads'])
		print 'full_house : ' + unicode(winning_tally['full_house'])
		print 'flush : ' + unicode(winning_tally['flush'])
		print 'straight : ' + unicode(winning_tally['straight'])
		print 'three_of_a_kind : ' + unicode(winning_tally['three_of_a_kind'])
		print 'two_pair : ' + unicode(winning_tally['two_pair'])
		print 'pair : ' + unicode(winning_tally['pair'])
		print 'high_card : ' + unicode(winning_tally['high_card'])

	return winning_tally

def main():
	# test_plo(num_players=9, debug=True)
	sim_dictionary = {}
	for i in range(2,10):
		# print i
		sim_dictionary[i] = run_simulation(500, i)
	for sim in sim_dictionary:
		print sim
		print 'straight_flush : \t' + unicode(sim_dictionary[sim]['straight_flush'])
		print 'quads : \t' + unicode(sim_dictionary[sim]['quads'])
		print 'full_house : \t' + unicode(sim_dictionary[sim]['full_house'])
		print 'flush : \t' + unicode(sim_dictionary[sim]['flush'])
		print 'straight : \t' + unicode(sim_dictionary[sim]['straight'])
		print 'three_of_a_kind : \t' + unicode(sim_dictionary[sim]['three_of_a_kind'])
		print 'two_pair : \t' + unicode(sim_dictionary[sim]['two_pair'])
		print 'pair : \t' + unicode(sim_dictionary[sim]['pair'])
		print 'high_card : \t' + unicode(sim_dictionary[sim]['high_card'])

if __name__ == '__main__':
	main()
