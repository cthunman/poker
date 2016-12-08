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
		pairedBoard = False
		setOnBoard = False
		quadsOnBoard = False

		valueDict = {}
		for card in cardList:
			if card not in valueDict:
				valueDict[card.value] = []
			valueDict[card.value].append(card)
		for k in valueDict:
			if len(valueDict[k]) == 2:
				pairedBoard = True
			elif len(valueDict[k]) == 3:
				setOnBoard = True
			elif len(valueDict[k]) == 4:
				quadsOnBoard = True

		# is there flush possibility?
		possibleFlush = False
		flushDict = {}
		for card in cardList:
			if card not in flushDict:
				flushDict[card.suit] = []
			flushDict[card.suit].append(card)
		for k in flushDict:
			if len(flushDict[k]) > 2:
				possibleFlush = True

		# is there straight possibility?
		straightDict = {}
		for i in range(5, 15):
			straightDict[i] = []
		print straightDict
		for card in cardList:
			if card.numeric_value == 14:
				straightDict[5].append(card)
				straightDict[14].append(card)
			else:
				j = card.numeric_value
				index = 0
				while j < 15 and index < 5:
					straightDict[j].append(card)
					j += 1
					index += 1
		possibleStraight = False
		for k in straightDict:
			if len(straightDict[k]) > 2:
				possibleStraight = True

		# for k in straightDict:
		# 	out = ''
		# 	for c in straightDict[k]:
		# 		out += unicode(c) + ' '
		# 	print k, out

		# is there straight flush possibility?

		# nuts is top set

	def straightDraws(self):
		pass

	def flushDraws(self):
		pass

def main():
	flop = [Card('AS'), Card('KS'), Card('QS')]
	board = PLOBoard(flop=flop)
	board.currentNuts()

if __name__ == '__main__':
	main()
