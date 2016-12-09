from Hand import Hand, Card
import random, itertools
from cards import cards

class PLOStartHand():
	def __init__(self, *args):
		self.cardList = []
		for arg in args:
			self.cardList.append(Card(arg))
		# else:
		# 	self.cardList = cardList

	def appendCard(self, card):
		self.cardList.append(card)

def main():
	hand = PLOStartHand('AS', 'KD', '5D', 'AC')
	for card in hand.cardList:
		print unicode(card), unicode(card.value), unicode(card.suit)

if __name__ == '__main__':
	main()
