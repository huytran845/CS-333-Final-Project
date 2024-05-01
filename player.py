#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

from card import Card

class Player:
	def __init__(self, playerName):
		self.name = playerName
		self.hand = []
	
	def addCardToHand(self, card):
		self.hand.append(card)

	def removeCardInHand(self, card):
		self.hand.remove(card)

	def hasValue(self, value):
		for card in self.hand:
			if card.value == value:
				return True
		return False
	
	def countNumValue(self, value):
		count = 0
		for card in self.hand:
			if card.value == value:
				count += 1
		return count
	
	def getBooks(self):
		books = []
		for value in Card.values:
			count = self.countNumValue(value)
			if count == 4:
				books.append(value)
		return books