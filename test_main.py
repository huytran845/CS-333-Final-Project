#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

import unittest
from gofish import GoFish
from player import Player
from card import Card
from deck import Deck

class TestGoFishIntegration(unittest.TestCase):
	playerNames = ["Player 1", "Player 2", "Player 3"]

	def test_cardDeckRelation(self):
		newDeck = Deck()
		testCard = Card("Ace", "Hearts")
		self.assertEqual(str(newDeck.deck[0]), str(testCard))
	
	def test_cardPlayerRelation(self):
		newPlayer = Player("Test Player")
		newPlayer = Player("Test Player")
		testCard = Card("10", "Hearts")
		testCard2 = Card("10", "Spades")
		testCard3 = Card("10", "Clubs")
		testCard4 = Card("10", "Diamonds")
		newPlayer.addCardToHand(testCard)
		self.assertEqual(str(newPlayer.hand[0]), "10 of Hearts")
		newPlayer.addCardToHand(testCard2)
		self.assertEqual(str(newPlayer.hand[1]), "10 of Spades")
		newPlayer.addCardToHand(testCard3)
		self.assertEqual(str(newPlayer.hand[2]), "10 of Clubs")
		newPlayer.addCardToHand(testCard4)
		self.assertEqual(str(newPlayer.hand[3]), "10 of Diamonds")
		self.assertEqual(newPlayer.getBooks(), ["10"])
	
	def test_deckGoFish(self):
		newGame = GoFish(3, self.playerNames)
		newDeck = Deck()
		self.assertEqual(len(newGame.startDeck.deck), len(newDeck.deck))
		newGame.startDeck.dealCard()
		self.assertNotEqual(len(newGame.startDeck.deck), len(newDeck.deck))

	def test_playerGoFish(self):
		newGame = GoFish(3, self.playerNames)
		testPlayer = Player("Test Player")
		testCard = Card("10", "Hearts")
		testCard2 = Card("10", "Spades")
		testCard3 = Card("10", "Clubs")
		testCard4 = Card("10", "Diamonds")
		testCard5 = Card("8", "Hearts")
		testCard6 = Card("8", "Spades")
		newGame.dealToPlayers()
		testPlayer.addCardToHand(testCard)
		testPlayer.addCardToHand(testCard2)
		testPlayer.addCardToHand(testCard3)
		testPlayer.addCardToHand(testCard4)
		testPlayer.addCardToHand(testCard5)
		testPlayer.addCardToHand(testCard6)
		testPlayer.addCardToHand(testCard6)
		self.assertNotEqual(str(newGame.players[0].hand), str(testPlayer.hand))
		self.assertEqual(len(newGame.players[0].hand), len(testPlayer.hand))

	def test_playerNames(self):
		newGame = GoFish(3, self.playerNames)
		self.assertEqual(newGame.players[0].name, self.playerNames[0])
		self.assertEqual(newGame.players[1].name, self.playerNames[1])
		self.assertEqual(newGame.players[2].name, self.playerNames[2])

	def test_cardGoFish(self):
		newGame = GoFish(3, self.playerNames)
		testCard = Card("10", "Hearts")
		newGame.players[0].addCardToHand(testCard)
		self.assertEqual(str(newGame.players[0].hand[0]), str(testCard))

	
if __name__ == '__main__':
    unittest.main()