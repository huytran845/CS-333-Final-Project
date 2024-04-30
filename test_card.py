#Author: Huy Tran
#CS 333 Testing Dev Ops
#2/26/2024

import unittest
from card import Card

class TestCardMethods(unittest.TestCase):
	def test_card(self):
		testCard = Card("10", "Hearts")
		self.assertEqual(testCard.value, "10")
		self.assertEqual(testCard.suit, "Hearts")
		

if __name__ == '__main__':
    unittest.main()