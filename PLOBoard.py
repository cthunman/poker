from Hand import Hand, Card
import random, itertools
from cards import cards

class PLOBoard():

	def __init__(self, flop=None, turn=None, river=None):
		self.flop = flop
		self.turn = turn
		self.river = river

	def currentNuts(self):
		cardList = []
		if self.flop != None:
			cardList.extend(self.flop)
		if self.turn != None:
			cardList.append(self.turn)
		if self.river != None:
			cardList.append(self.river)

		# is board paired?
		valueDict = {}
		for card in cardList:
			if card not in cardList:
				valueDict[card.value] = []
			valueDict[card.value].append(card)

		# is there flush possibility?
		flushDict = {}
		for card in cardList:
			if card not in cardList:
				flushDict[card.suit] = []
			flushDict[card.suit].append(card)

		# is there straight possibility?
		straightDict = {}
		for i in range(5, 15):
			straightDict[i] = []
		for card in cardList:
			if card.numeric_value == 14:
				straightDict[5].append(card)
				straightDict[14].append(card)
			else:
				j = card.numeric_value
				index = 0
				while j < 14 and index < 5:
					straightDict[j].append(card)

		# is there straight flush possibility?

		# nuts is top set

	def straightDraws(self):
		pass

	def flushDraws(self):
		pass

def main():
	print 'test'

if __name__ == '__main__':
	main()
