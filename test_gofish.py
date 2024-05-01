#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

import unittest
from gofish import GoFish

class TestGoFishMethods(unittest.TestCase):
	playerNames = ["Player 1", "Player 2", "Player 3"]

	def test_getCurrentPlayer(self):
		newGame = GoFish(3, self.playerNames)
		curPlayer = newGame.getCurrentPlayer()
		self.assertEqual(curPlayer.name, "Player 1")
	
	def test_advancePlayer(self):
		newGame = GoFish(3, self.playerNames)
		curPlayer = newGame.getCurrentPlayer()
		self.assertEqual(curPlayer.name, "Player 1")
		newGame.advancePlayer()
		curPlayer = newGame.getCurrentPlayer()
		self.assertEqual(curPlayer.name, "Player 2")
		newGame.advancePlayer()
		curPlayer = newGame.getCurrentPlayer()
		self.assertEqual(curPlayer.name, "Player 3")
		newGame.advancePlayer()
		curPlayer = newGame.getCurrentPlayer()
		self.assertEqual(curPlayer.name, "Player 1")

	def test_startingDealtHands(self):
		smallGame = GoFish(3, self.playerNames)
		smallGame.dealToPlayers()
		firstPlayer = smallGame.getCurrentPlayer()
		self.assertEqual(len(firstPlayer.hand), 7)
		self.playerNames.append("Player 4")
		self.playerNames.append("Player 5")
		bigGame = GoFish(5, self.playerNames)
		bigGame.dealToPlayers()
		firstPlayer = bigGame.getCurrentPlayer()
		self.assertEqual(len(firstPlayer.hand), 5)


if __name__ == '__main__':
    unittest.main()