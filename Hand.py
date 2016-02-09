import itertools

class Hand():
	# cards = []
	hierarchy = {
		'straight_flush' : 9,
		'quads' : 8,
		'full_house' : 7,
		'flush' : 6,
		'straight' : 5,
		'three_of_a_kind' : 4,
		'two_pair' : 3,
		'pair' : 2,
		'high_card' : 1,
	}
	# value = None

	def __init__(self, card_list):
		self.cards = card_list
		self.find_hand_type()

	def __unicode__(self):

		card_string = ''
		print 'self.cards'
		print self.cards
		for c in self.cards:
			print c
		for card in self.cards:
			card_string = card_string + ' ' + unicode(card)

	def is_straight_flush(self):
		if len(self.cards) == 5:
			return bool(self.is_flush()) and bool(self.is_straight())
		else:
			return False

	def is_flush(self):
		if len(self.cards) == 5:
			flush_suit = self.cards[0].suit
			for card in self.cards:
				if card.suit is not flush_suit:
					return False
			return True
		else:
			return False

	def is_straight(self):
		if len(self.cards) == 5:
			
			test_for_aces = next((card for card in self.cards if card.value == 'A'), None)
			if test_for_aces is None:
			# if True:
				sorted_cards = sorted(self.cards, key=lambda card: card.value)
				if (sorted_cards[0].numeric_value == sorted_cards[1].numeric_value - 1 and
						sorted_cards[1].numeric_value == sorted_cards[2].numeric_value - 1 and
						sorted_cards[2].numeric_value == sorted_cards[3].numeric_value - 1 and
						sorted_cards[3].numeric_value == sorted_cards[4].numeric_value - 1):
					return True
				else:
					return False
			# elif len(test_for_aces) > 1:
			# 	return False
			else:
				card_list_1 = []
				card_list_2 = []
				for card in self.cards:
					if card.value == 'A':
						card_list_1.append({ 'suit' : card.suit, 'value' : 1 })
						card_list_2.append({ 'suit' : card.suit, 'value' : 14 })
					elif card.value == 'K':
						card_list_1.append({ 'suit' : card.suit, 'value' : 13 })
						card_list_2.append({ 'suit' : card.suit, 'value' : 13 })
					elif card.value == 'Q':
						card_list_1.append({ 'suit' : card.suit, 'value' : 12 })
						card_list_2.append({ 'suit' : card.suit, 'value' : 12 })
					elif card.value == 'J':
						card_list_1.append({ 'suit' : card.suit, 'value' : 11 })
						card_list_2.append({ 'suit' : card.suit, 'value' : 11 })
					elif card.value == 'T':
						card_list_1.append({ 'suit' : card.suit, 'value' : 10 })
						card_list_2.append({ 'suit' : card.suit, 'value' : 10 })
					else:
						card_list_1.append({ 'suit' : card.suit, 'value' : int(card.value) })
						card_list_2.append({ 'suit' : card.suit, 'value' : int(card.value) })
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

	def has_quads(self):
		if len(self.cards) == 5:
			value_map = self.get_value_map()
			if 4 in value_map.values():
				return True
			else:
				return False
		else:
			return False

	def has_full_house(self):
		if len(self.cards) == 5:
			value_map = self.get_value_map()
			if 3 in value_map.values() and 2 in value_map.values():
				return True
			else:
				return False
		else:
			return False

	def has_set(self):
		if len(self.cards) == 5:
			value_map = self.get_value_map()
			if 3 in value_map.values():
				return True
			else:
				return False
		else:
			return False

	def has_two_pair(self):
		if len(self.cards) == 5:
			value_map = self.get_value_map()
			count = 0
			for value in value_map:
				if value_map[value] == 2:
					count += 1
			if count == 2:
				return True
			else:
				return False
		else:
			return False

	def has_pair(self):
		if len(self.cards) == 5:
			value_map = self.get_value_map()
			if 2 in value_map.values():
				return True
			else:
				return False
		else:
			return False

	def get_value_map(self):
		values = { 
			2 : 0,
			3 : 0,
			4 : 0,
			5 : 0,
			6 : 0,
			7 : 0,
			8 : 0,
			9 : 0,
			10 : 0,
			11 : 0,
			12 : 0,
			13 : 0,
			14 : 0,
		}
		for card in self.cards:
			if card.value == 'A':
				values[14] += 1
			elif card.value =='T':
				values[10] += 1
			elif card.value =='K':
				values[13] += 1
			elif card.value =='Q':
				values[12] += 1
			elif card.value =='J':
				values[11] += 1
			else:
				values[int(card.value)] += 1
		return values

	def find_hand_type(self):
		if self.is_straight_flush():
			self.value = 'straight_flush'
		elif self.has_quads():
			self.value = 'quads'
		elif self.has_full_house():
			self.value = 'full_house'
		elif self.is_flush():
			self.value = 'flush'
		elif self.is_straight():
			self.value = 'straight'
		elif self.has_set():
			self.value = 'three_of_a_kind'
		elif self.has_two_pair():
			self.value = 'two_pair'
		elif self.has_pair():
			self.value = 'pair'
		else:
			self.value = 'high_card'

	def compare_to_hand(self, hand):
		if self.hierarchy[self.value] > hand.hierarchy[hand.value]:
			return 1
		elif self.hierarchy[self.value] < hand.hierarchy[hand.value]:
			return -1
		elif self.hierarchy[self.value] == 9 and hand.hierarchy[hand.value] == 9:
			self_value_map = self.get_value_map()
			other_value_map = hand.get_value_map()

			self_value_list = []
			other_value_list = []

			for key in self_value_map:
				if self_value_map[key] == 1:
					self_value_list.append(key)
			for key in other_value_map:
				if other_value_map[key] == 1:
					other_value_list.append(key)
			self_value_list.sort()
			other_value_list.sort()
			self_value_list.reverse()
			other_value_list.reverse()

			if self_value_list[0] > other_value_list[0]:
				return 1
			elif other_value_list[0] > self_value_list[0]:
				return -1
			else:
				return 0

		# has_quads
		# compare which 4 of a kind is a higher card
		elif self.hierarchy[self.value] == 8 and hand.hierarchy[hand.value] == 8:
			self_value_map = self.get_value_map()
			other_value_map = hand.get_value_map()
			for value_key in self_value_map:
				if self_value_map[value_key] == 4:
					self_value = value_key
			for value_key in other_value_map:
				if other_value_map[value_key] == 4:
					other_value = value_key
			if self_value > other_value:
				return 1
			elif other_value > self_value:
				return -1
			else:
				for value_key in self_value_map:
					if self_value_map[value_key] == 1:
						self_value = value_key
				for value_key in other_value_map:
					if other_value_map[value_key] == 1:
						other_value = value_key
				if self_value > other_value:
					return 1
				elif other_value > self_value:
					return -1
				else:
					return 0

		# full_house
		# compare which three cards are higher... if they tie, compare the bottom two
		elif self.hierarchy[self.value] == 7 and hand.hierarchy[hand.value] == 7:
			self_value_map = self.get_value_map()
			other_value_map = hand.get_value_map()
			for value_key in self_value_map:
				if self_value_map[value_key] == 3:
					self_value = value_key
			for value_key in other_value_map:
				if other_value_map[value_key] == 3:
					other_value = value_key
			if self_value > other_value:
				return 1
			elif other_value > self_value:
				return -1
			else:
				for value_key in self_value_map:
					if self_value_map[value_key] == 2:
						self_value = value_key
				for value_key in other_value_map:
					if other_value_map[value_key] == 2:
						other_value = value_key
				if self_value > other_value:
					return 1
				elif other_value > self_value:
					return -1
				else:
					return 0
		
		# flush
		# compare which hand has highest card and keep comparing until one has a higher card
		elif self.hierarchy[self.value] == 6 and hand.hierarchy[hand.value] == 6:
			self_value_map = self.get_value_map()
			other_value_map = hand.get_value_map()

			self_value_list = []
			other_value_list = []

			for key in self_value_map:
				if self_value_map[key] == 1:
					self_value_list.append(key)
			for key in other_value_map:
				if other_value_map[key] == 1:
					other_value_list.append(key)

			self_value_list.sort()
			other_value_list.sort()
			return_val = 0
			for i in range(0,5):
				if self_value_list[i] > other_value_list[i]:
					return_val = 1
				elif other_value_list[i] > self_value_list[i]:
					return_val = -1
			return return_val

		# straight
		# compare which has the highest card
		elif self.hierarchy[self.value] == 5 and hand.hierarchy[hand.value] == 5:
			self_value_map = self.get_value_map()
			other_value_map = hand.get_value_map()

			self_value_list = []
			other_value_list = []

			for key in self_value_map:
				if self_value_map[key] == 1:
					self_value_list.append(key)
			for key in other_value_map:
				if other_value_map[key] == 1:
					other_value_list.append(key)
			self_value_list.sort()
			other_value_list.sort()
			self_value_list.reverse()
			other_value_list.reverse()

			if self_value_list[0] > other_value_list[0]:
				return 1
			elif other_value_list[0] > self_value_list[0]:
				return -1
			else:
				return 0

		# three_of_a_kind
		# compare which has higher 3 of a kind then compare kicker and last card
		elif self.hierarchy[self.value] == 4 and hand.hierarchy[hand.value] == 4:
			self_value_map = self.get_value_map()
			other_value_map = hand.get_value_map()
			for value_key in self_value_map:
				if self_value_map[value_key] == 3:
					self_value = value_key
			for value_key in other_value_map:
				if other_value_map[value_key] == 3:
					other_value = value_key
			if self_value > other_value:
				return 1
			elif other_value > self_value:
				return -1
			else:
				self_value_list = []
				other_value_list = []

				for key in self_value_map:
					if self_value_map[key] == 1:
						self_value_list.append(key)
				for key in other_value_map:
					if other_value_map[key] == 1:
						other_value_list.append(key)

				self_value_list.sort()
				other_value_list.sort()
				return_val = 0
				for i in range(0,2):
					if self_value_list[i] > other_value_list[i]:
						return_val = 1
					elif other_value_list[i] > self_value_list[i]:
						return_val = -1
				return return_val
		
		# two_pair
		# compare which has higher top pair then which has higher bottom pair then kicker		
		elif self.hierarchy[self.value] == 3 and hand.hierarchy[hand.value] == 3:
			self_value_map = self.get_value_map()
			other_value_map = hand.get_value_map()
			self_value_list = []
			other_value_list = []

			for key in self_value_map:
				if self_value_map[key] == 2:
					self_value_list.append(key)
			for key in other_value_map:
				if other_value_map[key] == 2:
					other_value_list.append(key)

			self_value_list.sort()
			other_value_list.sort()
			return_val = 0
			for i in range(0,2):
				if self_value_list[i] > other_value_list[i]:
					return_val = 1
				elif other_value_list[i] > self_value_list[i]:
					return_val = -1
			
			if return_val == 0:
				for key in self_value_map:
					if self_value_map[key] == 1:
						self_kicker = key
				for key in other_value_map:
					if other_value_map[key] == 1:
						other_kicker = key
				if self_kicker > other_kicker:
					return 1
				elif other_kicker > self_kicker:
					return -1
				else:
					return 0
			else:
				return return_val

		# pair
		# compare which has higher pair then compare kicker and other two cards
		elif self.hierarchy[self.value] == 2 and hand.hierarchy[hand.value] == 2:
			self_value_map = self.get_value_map()
			other_value_map = hand.get_value_map()
			for value_key in self_value_map:
				if self_value_map[value_key] == 2:
					self_value = value_key
			for value_key in other_value_map:
				if other_value_map[value_key] == 2:
					other_value = value_key
			if self_value > other_value:
				return 1
			elif other_value > self_value:
				return -1
			else:
				self_value_list = []
				other_value_list = []

				for key in self_value_map:
					if self_value_map[key] == 1:
						self_value_list.append(key)
				for key in other_value_map:
					if other_value_map[key] == 1:
						other_value_list.append(key)

				self_value_list.sort()
				other_value_list.sort()
				return_val = 0
				for i in range(0,3):
					if self_value_list[i] > other_value_list[i]:
						return_val = 1
					elif other_value_list[i] > self_value_list[i]:
						return_val = -1
				return return_val
		
		# high_card
		# compare in order from top to bottom which has highest card
		elif self.hierarchy[self.value] == 1 and hand.hierarchy[hand.value] == 1:
			self_value_map = self.get_value_map()
			other_value_map = hand.get_value_map()

			self_value_list = []
			other_value_list = []

			for key in self_value_map:
				if self_value_map[key] == 1:
					self_value_list.append(key)
			for key in other_value_map:
				if other_value_map[key] == 1:
					other_value_list.append(key)

			self_value_list.sort()
			other_value_list.sort()
			return_val = 0
			for i in range(0,3):
				if self_value_list[i] > other_value_list[i]:
					return_val = 1
				elif other_value_list[i] > self_value_list[i]:
					return_val = -1
			return return_val
		else:
			print 'WARNING: hands not valid'
			return False

class Card():

	def __init__(self, card_string):
		self.numeric_value_dict = {
			'2' : 2,
			'3' : 3,
			'4' : 4,
			'5' : 5,
			'6' : 6,
			'7' : 7,
			'8' : 8,
			'9' : 9,
			'T' : 10,
			'J' : 11,
			'Q' : 12,
			'K' : 13,
			'A' : 14,
		}
		self.value = card_string[0]
		self.suit = card_string[1]
		self.numeric_value = self.numeric_value_dict[self.value]

	def __unicode__(self):
		return unicode(self.value) + unicode(self.suit)
	def __str__(self):
		return unicode(self)

def main():

	card1 = Card('AS')
	card2 = Card('TS')
	card3 = Card('AC')
	card4 = Card('AH')
	card5 = Card('AD')

	card21 = Card('9S')
	card22 = Card('TC')
	card23 = Card('9C')
	card24 = Card('9H')
	card25 = Card('9D')

	card_list = [ card1, card2, card3, card4, card5, ]
	card_list2 = [ card21, card22, card23, card24, card25, ]
	hand = Hand(card_list)
	hand2 = Hand(card_list2)

	# card = Card('AS')
	# print card.value
	# print card.suit

	print hand.value + ' ' + unicode(hand.compare_to_hand(hand2))
	print hand2.value + ' ' + unicode(hand2.compare_to_hand(hand))

if __name__ == '__main__':
	main()
