from Hand import Hand, Card
import random

cards = [
	'2S',
	'3S',
	'4S',
	'5S',
	'6S',
	'7S',
	'8S',
	'9S',
	'TS',
	'JS',
	'QS',
	'KS',
	'AS',
	'2C',
	'3C',
	'4C',
	'5C',
	'6C',
	'7C',
	'8C',
	'9C',
	'TC',
	'JC',
	'QC',
	'KC',
	'AC',
	'2H',
	'3H',
	'4H',
	'5H',
	'6H',
	'7H',
	'8H',
	'9H',
	'TH',
	'JH',
	'QH',
	'KH',
	'AH',
	'2D',
	'3D',
	'4D',
	'5D',
	'6D',
	'7D',
	'8D',
	'9D',
	'TD',
	'JD',
	'QD',
	'KD',
	'AD',
]

def find_best_hand(cardlist):
	if len(cardlist) == 7:
		return True
	else:
		return None

def main():
	# cards = open('cards').readlines()
	cardlist = []
	for card in cards:
		cardlist.append(Card(card))
	random.shuffle(cardlist)
	# for card in cardlist:
	# 	print card
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

	index = 0
	for player in playerlist:
		card_string = ''
		for card in player['cards']:
			card_string += unicode(card) + ' '
		print 'Player' + unicode(index + 1) + ': ' + unicode(card_string)
		index += 1
	card_string = ''
	for card in shared_cards:
		card_string += unicode(card) + ' '
	print 'Shared cards: ' + card_string

if __name__ == '__main__':
	main()
