#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

import unittest
from player import Player
from card import Card

class TestPlayerMethods(unittest.TestCase):
	def test_addCardToHand(self):
		newPlayer = Player("Test Player")
		testCard = Card("10", "Hearts")
		newPlayer.addCardToHand(testCard)
		self.assertEqual(str(newPlayer.hand[0]), "10 of Hearts")

	def test_removeCardInHand(self):
		newPlayer = Player("Test Player")
		testCard = Card("10", "Hearts")
		newPlayer.addCardToHand(testCard)
		self.assertEqual(len(newPlayer.hand), 1)
		newPlayer.removeCardInHand(testCard)
		self.assertEqual(len(newPlayer.hand), 0)

	def test_removeSameCards(self):
		newPlayer = Player("Test Player")
		sameValCard1 = Card("10", "Hearts")
		sameValCard2 = Card("10", "Spades")
		testCard = Card("9", "Clubs")
		newPlayer.addCardToHand(sameValCard1)
		newPlayer.addCardToHand(sameValCard2)
		newPlayer.addCardToHand(sameValCard1)
		newPlayer.addCardToHand(sameValCard2)	
		newPlayer.addCardToHand(testCard)
		self.assertEqual(len(newPlayer.hand), 5)
		newPlayer.removeSameCards("10")
		self.assertEqual(len(newPlayer.hand), 1)

	def test_hasValue(self):
		newPlayer = Player("Test Player")
		testCard = Card("10", "Hearts")
		newPlayer.addCardToHand(testCard)
		self.assertTrue(newPlayer.hasValue("10"))

	def test_hasNoValue(self):
		newPlayer = Player("Test Player")
		testCard = Card("10", "Hearts")
		newPlayer.addCardToHand(testCard)
		self.assertFalse(newPlayer.hasValue("Ace"))
	
	def test_countNumValues(self):
		newPlayer = Player("Test Player")
		testCard = Card("10", "Hearts")
		testCard2 = Card("10", "Spades")
		testCard3 = Card("1", "Hearts")
		newPlayer.addCardToHand(testCard)
		newPlayer.addCardToHand(testCard2)
		newPlayer.addCardToHand(testCard3)
		self.assertEqual(newPlayer.countNumValue("10"), 2)

	def test_getBooks(self):
		newPlayer = Player("Test Player")
		testCard = Card("10", "Hearts")
		testCard2 = Card("10", "Spades")
		testCard3 = Card("10", "Clubs")
		testCard4 = Card("10", "Diamonds")
		newPlayer.addCardToHand(testCard)
		newPlayer.addCardToHand(testCard2)
		newPlayer.addCardToHand(testCard3)
		newPlayer.addCardToHand(testCard4)
		self.assertEqual(newPlayer.getBooks(), ["10"])

if __name__ == '__main__':
    unittest.main()