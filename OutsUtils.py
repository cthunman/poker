from Hand import Hand, Card
import random, itertools
from cards import cards
from decimal import *
import copy

class Path():
	def __init__(self, outsLists):
		self.outsLists = outsLists

	def calculateOdds(self, cardsToCome, numUnknowns, outsLists):
		currentOutsLists = []
		totalCardsNeeded = 0
		for outsList in outsLists:
			totalCardsNeeded += outsList.numNeeded
			if outsList.numNeeded > 0:
				currentOutsLists.append(outsList)

		if totalCardsNeeded > cardsToCome:
			return 0.0
		
		if cardsToCome == 1:
			return Decimal(currentOutsLists[0].numCards)/Decimal(numUnknowns)
		else:
			oddsSum = Decimal(0)
			for i in range(len(currentOutsLists)):
				newOutsLists = copy.deepcopy(currentOutsLists)
				newOutsLists[i].numNeeded -= 1
				newOutsLists[i].numCards -= 1
				oddsSoFar = Decimal(currentOutsLists[i].numCards)/Decimal(numUnknowns)
				oddsSum += oddsSoFar * (self.calculateOdds(cardsToCome - 1, numUnknowns - 1, newOutsLists))
			return oddsSum

class OutsList():
	def __init__(self, numCards, numNeeded):
		self.numCards = numCards
		self.numNeeded = numNeeded

def main():
	outsList = OutsList(6, 1)
	missesList = OutsList(44, 2)
	path = Path([outsList, missesList])
	outsLists = path.outsLists
	print 'flop one pair NLH: ' + unicode(path.calculateOdds(3, 50, outsLists))

	firstPair = OutsList(3, 1)
	secondPair = OutsList(3, 1)
	missesList = OutsList(44, 1)
	path = Path([firstPair, secondPair, missesList])
	outsLists = path.outsLists
	print 'flop two pair NLH: ' + unicode(path.calculateOdds(3, 50, outsLists))

	outsList = OutsList(6, 1)
	missesList = OutsList(44, 4)
	path = Path([outsList, missesList])
	outsLists = path.outsLists
	print 'one pair by the river NLH: ' + unicode(path.calculateOdds(5, 50, outsLists))

	firstPair = OutsList(3, 2)
	secondPair = OutsList(3, 1)
	# missesList = OutsList(44, 0)
	path = Path([firstPair, secondPair])
	outsLists = path.outsLists
	print 'flop two pair NLH: ' + unicode(path.calculateOdds(3, 50, outsLists) * 2)

if __name__ == '__main__':
	main()
