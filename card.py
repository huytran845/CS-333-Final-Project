#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

class Card:
	values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

	def __init__(self, newValue, newSuit):
		self.suit = newSuit
		self.value = newValue

	def __repr__(self) -> str:
		return self.value + " of " + self.suit