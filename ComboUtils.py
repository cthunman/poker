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
		playerlist.append({'cards':[]})

	hand_record['starting_hands'] = {}
	for index, player in enumerate(playerlist):
		player['cards'].append(cardlist.pop())
		player['cards'].append(cardlist.pop())
		hand_record['starting_hands'][index + 1] = []
		for c in player['cards']:
			hand_record['starting_hands'][index + 1].append(unicode(c))
		if file != None:
			file.write('player' + unicode(index + 1) + ': ')
			for c in player['cards']:
				file.write(unicode(c) + ' ')
			file.write('\n')

	shared_cards = []
	shared_cards.append(cardlist.pop())
	shared_cards.append(cardlist.pop())
	shared_cards.append(cardlist.pop())
	shared_cards.append(cardlist.pop())
	shared_cards.append(cardlist.pop())
	hand_record['shared_cards'] = []
	for c in shared_cards:
		hand_record['shared_cards'].append(unicode(c))
	hand_record['flop'] = []
	for c in shared_cards[0:3]:
		hand_record['flop'].append(unicode(c))
	hand_record['turn'] = unicode(shared_cards[3])
	hand_record['river'] = unicode(shared_cards[4])

	if file != None:
		file.write('shared cards: ')
		for c in shared_cards:
			file.write(unicode(c) + ' ')
		file.write('\n')

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
		best_hand = find_best_hand(card_set)
		player_hands.append(best_hand)
		if debug:
			print unicode(best_hand)

		combos = itertools.combinations(card_set, 5)
		for combo in combos:
			card_string = ''
			for c in combo:
				card_string += unicode(c) + ' '
	hand_record['player_hands'] = {}
	for index, h in enumerate(player_hands):
		hand_record['player_hands'][index + 1] = unicode(h)
		file.write('player ' + unicode(index + 1) + ': ' + unicode(h) + ' \n')

	winner = find_winner(player_hands)
	hand_record['winner'] = {}
	hand_record['winner']['hand'] = []
	if len(winner) > 1:
		file.write('SPLIT POT: ')
		hand_record['winner']['status'] = 'SPLIT POT'
		for w in winner:
			file.write(unicode(w) + ' ')
			hand_record['winner']['hand'].append(unicode(w))
	else:
		file.write('WINNER: ')
		hand_record['winner']['status'] = 'WINNER'
		hand_record['winner']['hand'].append(unicode(winner[0]))
		file.write(unicode(winner[0]))
	file.write('\n\n')
	file.write(unicode(hand_record))
	file.write('\n\n')

	return find_winner(player_hands), player_hands

def test_plo(num_players=4, debug=False):
	cardlist = []
	for card in cards:
		cardlist.append(Card(card))
	random.shuffle(cardlist)
	
	playerlist = []
	for p in range(num_players):
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
	return find_winner(player_hands), player_hands

def test_big_o(num_players=4, debug=False):
	cardlist = []
	for card in cards:
		cardlist.append(Card(card))
	random.shuffle(cardlist)
	
	playerlist = []
	for p in range(num_players):
		playerlist.append({'cards':[]})

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
	return find_winner(player_hands), player_hands

def run_simulation(runs=1000, num_players=6, game='nlh', debug=False):
	winning_tally = {}
	winning_tally['straight_flush'] = {'tally': 0, 'ties': 0}
	winning_tally['quads'] = {'tally': 0, 'ties': 0}
	winning_tally['full_house'] = {'tally': 0, 'ties': 0}
	winning_tally['flush'] = {'tally': 0, 'ties': 0}
	winning_tally['straight'] = {'tally': 0, 'ties': 0}
	winning_tally['three_of_a_kind'] = {'tally': 0, 'ties': 0}
	winning_tally['two_pair'] = {'tally': 0, 'ties': 0}
	winning_tally['pair'] = {'tally': 0, 'ties': 0}
	winning_tally['high_card'] = {'tally': 0, 'ties': 0}

	player_hand_tally = {}
	player_hand_tally['straight_flush'] = {'tally': 0}
	player_hand_tally['quads'] = {'tally': 0}
	player_hand_tally['full_house'] = {'tally': 0}
	player_hand_tally['flush'] = {'tally': 0}
	player_hand_tally['straight'] = {'tally': 0}
	player_hand_tally['three_of_a_kind'] = {'tally': 0}
	player_hand_tally['two_pair'] = {'tally': 0}
	player_hand_tally['pair'] = {'tally': 0}
	player_hand_tally['high_card'] = {'tally': 0}

	f = open('data/db' + unicode(num_players) + '.txt', 'wb+')
	for i in range(runs):
		if runs > 500 and i % 500 == 0: print i 
		
		if game == 'nlh':
			winning_hands, player_hands = test_nlh(num_players=num_players, file=f)
		elif game == 'plo':
			winning_hands, player_hands = test_plo(num_players=num_players)
		winning_tally[winning_hands[0].value]['tally'] = winning_tally[winning_hands[0].value]['tally'] + 1
		if len(winning_hands) > 1:
			winning_tally[winning_hands[0].value]['ties'] = winning_tally[winning_hands[0].value]['ties'] + 1
		

		for h in player_hands:
			player_hand_tally[h.value]['tally'] = player_hand_tally[h.value]['tally'] + 1

	f.close()

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

	return winning_tally, player_hand_tally

def find_winners(runs=1000, num_players=6, debug=False):
	starting_hands = {}
	for i in range(runs):
		if runs > 500 and i % 500 == 0: print i

def main():
	# test_plo(num_players=9, debug=True)
	sim_dictionary = {}
	player_dictionary = {}
	runs = 5000
	for i in range(9, 10):
		sim_dictionary[i], player_dictionary[i] = run_simulation(runs, i, game='plo')
	column_width = 17

	print '--------------'
	for sim in sim_dictionary:
		print sim
		print 'straight_flush' + ' ' * (column_width - len('straight_flush')) + ' : ' + unicode(sim_dictionary[sim]['straight_flush']['tally']) + ' : ' + unicode(sim_dictionary[sim]['straight_flush']['ties']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['straight_flush']['tally']/float(runs)), 2)) + '%'
		if float(player_dictionary[sim]['straight_flush']['tally']) != 0:
			print 'straight_flush' + ' ' * (column_width - len('straight_flush')) + ' : ' + unicode(player_dictionary[sim]['straight_flush']['tally']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['straight_flush']['tally'])/float(player_dictionary[sim]['straight_flush']['tally']), 2)) + '%'
		else:
			print 'straight_flush' + ' ' * (column_width - len('straight_flush')) + ' : ' + unicode(player_dictionary[sim]['straight_flush']['tally']) + ' : 0.0%'
		print 'quads' + ' ' * (column_width - len('quads')) + ' : ' + unicode(sim_dictionary[sim]['quads']['tally']) + ' : ' + unicode(sim_dictionary[sim]['quads']['ties']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['quads']['tally']/float(runs)), 2)) + '%'
		if float(player_dictionary[sim]['quads']['tally']) != 0:
			print 'quads' + ' ' * (column_width - len('quads')) + ' : ' + unicode(player_dictionary[sim]['quads']['tally']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['quads']['tally'])/float(player_dictionary[sim]['quads']['tally']), 2)) + '%'
		else:
			print 'quads' + ' ' * (column_width - len('quads')) + ' : ' + unicode(player_dictionary[sim]['quads']['tally']) + ' : 0.0%'
		print 'full_house' + ' ' * (column_width - len('full_house')) + ' : ' + unicode(sim_dictionary[sim]['full_house']['tally']) + ' : ' + unicode(sim_dictionary[sim]['full_house']['ties']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['full_house']['tally']/float(runs)), 2)) + '%'
		if float(player_dictionary[sim]['full_house']['tally']) != 0:
			print 'full_house' + ' ' * (column_width - len('full_house')) + ' : ' + unicode(player_dictionary[sim]['full_house']['tally']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['full_house']['tally'])/float(player_dictionary[sim]['full_house']['tally']), 2)) + '%'
		else:
			print 'full_house' + ' ' * (column_width - len('full_house')) + ' : ' + unicode(player_dictionary[sim]['full_house']['tally']) + ' : 0.0%'
		print 'flush' + ' ' * (column_width - len('flush')) + ' : ' + unicode(sim_dictionary[sim]['flush']['tally']) + ' : ' + unicode(sim_dictionary[sim]['flush']['ties']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['flush']['tally']/float(runs)), 2)) + '%'
		if float(player_dictionary[sim]['flush']['tally']) != 0:
			print 'flush' + ' ' * (column_width - len('flush')) + ' : ' + unicode(player_dictionary[sim]['flush']['tally']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['flush']['tally'])/float(player_dictionary[sim]['flush']['tally']), 2)) + '%'
		else:
			print 'flush' + ' ' * (column_width - len('flush')) + ' : ' + unicode(player_dictionary[sim]['flush']['tally']) + ' : 0.0%'
		print 'straight' + ' ' * (column_width - len('straight')) + ' : ' + unicode(sim_dictionary[sim]['straight']['tally']) + ' : ' + unicode(sim_dictionary[sim]['straight']['ties']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['straight']['tally']/float(runs)), 2)) + '%'
		if float(player_dictionary[sim]['straight']['tally']) != 0:
			print 'straight' + ' ' * (column_width - len('straight')) + ' : ' + unicode(player_dictionary[sim]['straight']['tally']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['straight']['tally'])/float(player_dictionary[sim]['straight']['tally']), 2)) + '%'
		else:
			print 'straight' + ' ' * (column_width - len('straight')) + ' : ' + unicode(player_dictionary[sim]['straight']['tally']) + ' : 0.0%'
		print 'three_of_a_kind' + ' ' * (column_width - len('three_of_a_kind')) + ' : ' + unicode(sim_dictionary[sim]['three_of_a_kind']['tally']) + ' : ' + unicode(sim_dictionary[sim]['three_of_a_kind']['ties']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['three_of_a_kind']['tally']/float(runs)), 2)) + '%'
		if float(player_dictionary[sim]['three_of_a_kind']['tally']) != 0:
			print 'three_of_a_kind' + ' ' * (column_width - len('three_of_a_kind')) + ' : ' + unicode(player_dictionary[sim]['three_of_a_kind']['tally']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['three_of_a_kind']['tally'])/float(player_dictionary[sim]['three_of_a_kind']['tally']), 2)) + '%'
		else:
			print 'three_of_a_kind' + ' ' * (column_width - len('three_of_a_kind')) + ' : ' + unicode(player_dictionary[sim]['three_of_a_kind']['tally']) + ' : 0.0%'
		print 'two_pair' + ' ' * (column_width - len('two_pair')) + ' : ' + unicode(sim_dictionary[sim]['two_pair']['tally']) + ' : ' + unicode(sim_dictionary[sim]['two_pair']['ties']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['two_pair']['tally']/float(runs)), 2)) + '%'
		if float(player_dictionary[sim]['two_pair']['tally']) != 0:
			print 'two_pair' + ' ' * (column_width - len('two_pair')) + ' : ' + unicode(player_dictionary[sim]['two_pair']['tally']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['two_pair']['tally'])/float(player_dictionary[sim]['two_pair']['tally']), 2)) + '%'
		else:
			print 'two_pair' + ' ' * (column_width - len('two_pair')) + ' : ' + unicode(player_dictionary[sim]['two_pair']['tally']) + ' : 0.0%'
		print 'pair' + ' ' * (column_width - len('pair')) + ' : ' + unicode(sim_dictionary[sim]['pair']['tally']) + ' : ' + unicode(sim_dictionary[sim]['pair']['ties']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['pair']['tally']/float(runs)), 2)) + '%'
		if float(player_dictionary[sim]['pair']['tally']) != 0:
			print 'pair' + ' ' * (column_width - len('pair')) + ' : ' + unicode(player_dictionary[sim]['pair']['tally']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['pair']['tally'])/float(player_dictionary[sim]['pair']['tally']), 2)) + '%'
		else:
			print 'pair' + ' ' * (column_width - len('pair')) + ' : ' + unicode(player_dictionary[sim]['pair']['tally']) + ' : 0.0%'
		print 'high_card' + ' ' * (column_width - len('high_card')) + ' : ' + unicode(sim_dictionary[sim]['high_card']['tally']) + ' : ' + unicode(sim_dictionary[sim]['high_card']['ties']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['high_card']['tally']/float(runs)), 2)) + '%'
		if float(player_dictionary[sim]['high_card']['tally']) != 0:
			print 'high_card' + ' ' * (column_width - len('high_card')) + ' : ' + unicode(player_dictionary[sim]['high_card']['tally']) + ' : ' + unicode(round(100 * float(sim_dictionary[sim]['high_card']['tally'])/float(player_dictionary[sim]['high_card']['tally']), 2)) + '%'
		else:
			print 'high_card' + ' ' * (column_width - len('high_card')) + ' : ' + unicode(player_dictionary[sim]['high_card']['tally']) + ' : 0.0%'

if __name__ == '__main__':
	main()
