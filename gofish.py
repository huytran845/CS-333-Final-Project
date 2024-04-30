#Author: Huy Tran
#CS 333 Testing Dev Ops
#2/26/2024

from player import Player
from deck import Deck
from card import Card

class GoFish:
	def __init__(self, numPlayers, playerNames):
		self.startDeck = Deck()
		self.startDeck.shuffleDeck()
		self.players = []
		self.currentPlayer = 0
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