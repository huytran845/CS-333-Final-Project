#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

import random
from card import Card

class Deck:
	def __init__(self):
		self.deck = []
		self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
		self.values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

		for i in range(len(self.suits)):
			for j in range(len(self.values)):
				self.deck.append(Card(self.values[j], self.suits[i]))
	
	def shuffleDeck(self):
		random.shuffle(self.deck)

	def dealCard(self):
		if len(self.deck) == 0:
			return None
		else:	
			return self.deck.pop()