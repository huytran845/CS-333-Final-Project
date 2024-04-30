#Author: Huy Tran
#CS 333 Testing Dev Ops
#2/26/2024

import unittest
from player import Player
from card import Card

class TestPlayerMethods(unittest.TestCase):
	def test_addAceToHand(self):
		newPlayer = Player()
		testCard = Card("10", "Spades")
		aceCard = Card("Ace", "Hearts")

		newPlayer.addCardToHand(testCard)
		newPlayer.addCardToHand(aceCard)
		self.assertEqual(newPlayer.handValue, 21) #Ace becomes 11 since it doesn't bust the player
		newPlayer.addCardToHand(aceCard)
		self.assertEqual(newPlayer.handValue, 22) #Ace is 1 since 11 would significantly overbust the player

	def test_addFaceToHand(self):
		newPlayer = Player()
		testCard = Card("Jack", "Clubs")
		newPlayer.addCardToHand(testCard)
		self.assertEqual(newPlayer.handValue, 10) #Every instance of a face card should always just add 10 to the value
		testCard = Card("Queen", "Diamonds")
		newPlayer.addCardToHand(testCard)
		self.assertEqual(newPlayer.handValue, 20)
		testCard = Card("King", "Spades")
		newPlayer.addCardToHand(testCard)
		self.assertEqual(newPlayer.handValue, 30)

	def test_addNumberToHand(self):
		newPlayer = Player()
		testCard = Card("10", "Hearts")
		newPlayer.addCardToHand(testCard)
		self.assertEqual(newPlayer.handValue, 10)
		testCard = Card("2", "Hearts")
		newPlayer.addCardToHand(testCard)
		self.assertEqual(newPlayer.handValue, 12)
		testCard = Card("4", "Hearts")
		newPlayer.addCardToHand(testCard)
		self.assertEqual(newPlayer.handValue, 16)


if __name__ == '__main__':
    unittest.main()