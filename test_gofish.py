#Author: Huy Tran
#CS 333 Testing Dev Ops
#2/26/2024

import unittest
from gofish import GoFish
from player import Player
from card import Card
from deck import Deck

class TestGoFishMethods(unittest.TestCase):
	def test_setupHands(self):
		newGame = GoFish()
		playerHand = Player()
		dealerHand = Player(curDealer=True)
		self.assertEqual(len(playerHand.hand), 0)
		self.assertEqual(len(dealerHand.hand), 0)
		newGame.setupHands(playerHand, dealerHand)
		self.assertEqual(len(playerHand.hand), 2)
		self.assertEqual(len(dealerHand.hand), 2)

	def test_checkPlayer(self):
		newGame = GoFish()
		newPlayer = Player()
		testCard = Card("10", "Hearts")
		newPlayer.addCardToHand(testCard)
		self.assertFalse(newGame.checkPlayer(newPlayer))
		self.assertEqual(newPlayer.hand[0], testCard)
		newPlayer.addCardToHand(testCard)
		self.assertFalse(newGame.checkPlayer(newPlayer))
		newPlayer.addCardToHand(testCard)
		self.assertTrue(newGame.checkPlayer(newPlayer))

	def test_checkDealerBust(self):
		newGame = GoFish()
		player = Player()
		dealer = Player(curDealer=True)
		testCard = Card("10", "Hearts")
		dealer.addCardToHand(testCard)
		dealer.addCardToHand(testCard)
		dealer.addCardToHand(testCard)
		self.assertEqual(newGame.checkResult(dealer, player), 0)
		self.assertEqual

	def test_checkDealerWin(self):
		newGame = GoFish()
		player = Player()
		dealer = Player(curDealer=True)
		testCard = Card("10", "Hearts")
		dealer.addCardToHand(testCard)
		dealer.addCardToHand(testCard)
		player.addCardToHand(testCard)
		self.assertEqual(newGame.checkResult(dealer, player), 1)
		
	def test_checkDealerLose(self):
		newGame = GoFish()
		player = Player()
		dealer = Player(curDealer=True)
		testCard = Card("10", "Hearts")
		dealer.addCardToHand(testCard)
		player.addCardToHand(testCard)
		player.addCardToHand(testCard)
		self.assertEqual(newGame.checkResult(dealer, player), 2)
		
	def test_checkTie(self):
		newGame = GoFish()
		player = Player()
		dealer = Player(curDealer=True)
		testCard = Card("10", "Hearts")
		dealer.addCardToHand(testCard)
		dealer.addCardToHand(testCard)
		dealer.addCardToHand(testCard)
		self.assertEqual(newGame.checkResult(dealer, player), 0)

	# Integration Tests
	def test_cardPlayerRelation(self):
		newPlayer = Player() 
		newCard = Card("10", "Clubs")
		newPlayer.addCardToHand(newCard)
		self.assertEqual(newPlayer.handValue, int(newCard.value))

	def test_cardDeckRelation(self):
		newDeck = Deck()
		newCard = Card("Ace", "Hearts")
		self.assertEqual(str(newCard), str(newDeck.deck[0]))

	def test_blackjackDeckRelation(self):
		newGame = GoFish()
		newDeck = Deck()
		self.assertNotEqual(newGame.startDeck.deck[0], newDeck.deck[0])

if __name__ == '__main__':
    unittest.main()