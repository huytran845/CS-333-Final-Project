#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

from player import Player
from deck import Deck

class GoFish:
	values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

	def __init__(self, numPlayers, playerNames):
		self.startDeck = Deck()
		self.startDeck.shuffleDeck()
		self.players = []
		self.removedPlayers = []
		self.currentPlayer = 0
		self.books = 0
		for i in range(numPlayers):
			name = playerNames[i]
			newPlayer = Player(name)
			self.players.append(newPlayer)

	def getCurrentPlayer(self):
		return self.players[self.currentPlayer]

	def advancePlayer(self):
		if self.currentPlayer == len(self.players)-1:
			self.currentPlayer = 0
		else:
			self.currentPlayer = self.currentPlayer + 1

	def dealToPlayers(self):
		cardsDealt = 0
		if len(self.players) <= 3:
			cardsDealt = 7
		else:
			cardsDealt = 5
		for i in range (cardsDealt):
			for player in self.players:
				player.addCardToHand(self.startDeck.dealCard())

	def finishPlayers(self, player):
		self.players.remove(player)
		self.removedPlayers.append(player)