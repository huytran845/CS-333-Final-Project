#Author: Huy Tran
#CS 333 Testing Dev Ops
#2/26/2024

import unittest
from deck import Deck
from card import Card

class TestDeckMethods(unittest.TestCase):
	def test_dealCard(self):
		newDeck = Deck()
		testCard = Card("King", "Clubs")
		dealtCard = newDeck.dealCard()
		self.assertEqual(dealtCard.value, testCard.value)
		self.assertEqual(dealtCard.suit, testCard.suit)

	def test_shuffleDeck(self):
		normalDeck = Deck()
		shuffledDeck = Deck()
		shuffledDeck.shuffleDeck()
		self.assertNotEqual(normalDeck.deck, shuffledDeck.deck)

if __name__ == '__main__':
    unittest.main()