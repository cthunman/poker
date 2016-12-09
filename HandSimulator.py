from Hand import Hand, Card
from PLOStartHand import PLOStartHand
import random, itertools
from cards import cards
from collections import OrderedDict
from ComboUtils import *

class PLOHandSimulator():
	def __init__(self, handList, numPlayers, flop=None, turn=None, debug=True):
		self.handList = handList
		self.numPlayers = numPlayers
		self.debug = debug

	def simulate(self, runs):
		cardList = []
		cardDict = OrderedDict()
		for card in cards:
			c = Card(card)
			cardDict[card] = c

		for hand in self.handList:
			for card in hand.cardList:
				del cardDict[unicode(card)]
		
		for card in cardDict:
			cardList.append(cardDict[card])

		handStats = {}
		for hand in self.handList:
			handStats[hand] = {
				'wins': 0,
				'handsPlayed': 0,
				'bestHandList': []
			}

		for i in range(runs):
			if self.debug:
				print 'run ' + unicode(i)
			idx = 0
			random.shuffle(cardList)
			handDict = {}
			# deal cards
			for i in range(len(self.handList)):
				if i not in handDict:
					handDict[i] = {}
				handDict[i]['cards'] = self.handList[i].cardList
			for i in range(len(self.handList), self.numPlayers):
				if i not in handDict:
					handDict[i] = {'cards':[]}
				for j in range(4):
					handDict[i]['cards'].append(cardList[idx])
					idx += 1

			if self.debug:
				for h in handDict:
					hand = ''
					for c in handDict[h]['cards']:
						hand += unicode(c) + ' '
					print h, hand
			# deal board
			sharedCards = []
			for i in range(5):
				sharedCards.append(cardList[idx])
				idx += 1
			if self.debug:
				hand = ''
				for c in sharedCards:
					hand += unicode(c) + ' '
				print 'board ' + unicode(hand)
			madeHandDict = {}
			player_hands = []
			for player in handDict:
				best_hand = find_best_plo_hand(handDict[player]['cards'], sharedCards)
				player_hands.append(best_hand)
				madeHandDict[player] = best_hand

			if self.debug:
				print 'winner'
				for w in find_winner_seat(madeHandDict):
					print '\t' + unicode(w[0]) + ' : ' + unicode(w[1])

def main():
	hand1 = PLOStartHand('AS', 'KD', 'KC', 'AC')
	hand2 = PLOStartHand('AD', 'KS', 'KH', 'AH')

	s = PLOHandSimulator([hand1, hand2], 9, debug=True)
	s.simulate(10)

if __name__ == '__main__':
	main()
