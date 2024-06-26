#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

import unittest
from card import Card

class TestCardMethods(unittest.TestCase):
	def test_card(self):
		testCard = Card("10", "Hearts")
		self.assertEqual(testCard.value, "10")
		self.assertEqual(testCard.suit, "Hearts")
	
	def test_cardName(self):
		testCard = Card("10", "Hearts")
		self.assertEqual(str(testCard), "10 of Hearts")
		

if __name__ == '__main__':
    unittest.main()