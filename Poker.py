class Hand():
	cards = []

	def __init__(self, card_list):
		self.cards = card_list

	def is_straight_flush(self):
		if len(self.cards) == 5:
			return bool(self.is_flush()) and bool(self.is_straight())
		else:
			return False

	def is_flush(self):
		if len(self.cards) == 5:
			flush_suit = self.cards[0]['suit']
			for card in self.cards:
				if card['suit'] is not flush_suit:
					return False
			return True
		else:
			return False

	def is_straight(self):
		if len(self.cards) == 5:
			
			test_for_aces = next((card for card in self.cards if card['value'] == 'A'), None)
			# print len(test_for_aces)
			# print test_for_aces
			if test_for_aces is None:
			# if True:
				sorted_cards = sorted(self.cards, key=lambda card: card['value'])
				if (sorted_cards[0]['value'] == sorted_cards[1]['value'] - 1 and
						sorted_cards[1]['value'] == sorted_cards[2]['value'] - 1 and
						sorted_cards[2]['value'] == sorted_cards[3]['value'] - 1 and
						sorted_cards[3]['value'] == sorted_cards[4]['value'] - 1):
					return True
				else:
					return False
			# elif len(test_for_aces) > 1:
			# 	return False
			else:
				card_list_1 = []
				card_list_2 = []
				for card in self.cards:
					if card['value'] == 'A':
						card_list_1.append({ 'suit' : card['suit'], 'value' : 1 })
						card_list_2.append({ 'suit' : card['suit'], 'value' : 14 })
					else:
						card_list_1.append({ 'suit' : card['suit'], 'value' : card['value'] })
						card_list_2.append({ 'suit' : card['suit'], 'value' : card['value'] })
				sorted_cards_1 = sorted(card_list_1, key=lambda card: card['value'])
				sorted_cards_2 = sorted(card_list_2, key=lambda card: card['value'])
				if (sorted_cards_1[0]['value'] == sorted_cards_1[1]['value'] - 1 and
						sorted_cards_1[1]['value'] == sorted_cards_1[2]['value'] - 1 and
						sorted_cards_1[2]['value'] == sorted_cards_1[3]['value'] - 1 and
						sorted_cards_1[3]['value'] == sorted_cards_1[4]['value'] - 1) or (
						sorted_cards_2[0]['value'] == sorted_cards_2[1]['value'] - 1 and
						sorted_cards_2[1]['value'] == sorted_cards_2[2]['value'] - 1 and
						sorted_cards_2[2]['value'] == sorted_cards_2[3]['value'] - 1 and
						sorted_cards_2[3]['value'] == sorted_cards_2[4]['value'] - 1):
					return True
				else:
					return False
		else:
			return False

def main():

	card1 = { 'suit' : 'clubs', 'value' : 10 }
	card2 = { 'suit' : 'clubs', 'value' : 11 }
	card3 = { 'suit' : 'clubs', 'value' : 'A' }
	card4 = { 'suit' : 'clubs', 'value' : 12 }
	card5 = { 'suit' : 'clubs', 'value' : 13 }

	card_list = [ card1, card2, card3, card4, card5, ]
	hand = Hand(card_list)

	if hand.is_straight_flush():
		print 'straight flush'
	elif hand.is_flush():
		print 'flush'
	elif hand.is_straight():
		print 'straight'

if __name__ == '__main__':
	main()
