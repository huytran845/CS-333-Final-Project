#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

from gofish import GoFish
from card import Card

def main():
	print("Why, Hello There")
	while True:
		try:
			numPlayers = int(input("How many people are playing? "))
			break
		except ValueError:
			print("Invalid value, please enter a number!")

	playerNames = []
	for i in range(numPlayers):
		playerNames.append(input("Enter Player " + str(i+1) + "'s Name: "))

	goFish = GoFish(numPlayers, playerNames)
	goFish.dealToPlayers()

	while True:
		currentPlayer = goFish.getCurrentPlayer()

		print("\nCards in " + currentPlayer.name + "'s hand:")
		for card in currentPlayer.hand:
			print(card)

		currentBooks = currentPlayer.getBooks()
		for book in currentBooks:
			print("\n" + currentPlayer.name + " has acquired four of " + book + "s!")
			for player in goFish.players:
				if player != currentPlayer:
					player.removeCardInHand(Card("", book))
		
		requestedValue = input("\n" + currentPlayer.name + ", what card value would you like to ask for? Ace, 2-10, Jack-King: ")
		currentValues = [card.value for card in currentPlayer.hand]
		if not requestedValue in Card.values:
			print("Invalid value! Please try again!")
			continue
		elif not requestedValue in currentValues:
			print("You don't have any " + requestedValue + "s in your hand! Please try again!")
			continue
		
		while True:
			try:
				requestedPlayer = int(input("Choose a player to ask, enter a number: ")) - 1
				if requestedPlayer >= len(goFish.players) or requestedPlayer < 0:
					print("Player doesn't exist in this game!")
				elif requestedPlayer == goFish.currentPlayer:
					print("You can't pick yourself!")
				else:
					break
			except ValueError:
				print("Invalid player input, please enter a number!")
		
		selectedPlayer = goFish.players[requestedPlayer]
		if not selectedPlayer.hasValue(requestedValue):
			print(selectedPlayer.name + " doesn't have any " + requestedValue + "s, Go Fish!")
			dealtCard = goFish.startDeck.dealCard()
			if dealtCard is None:
				print("There are no cards remaining in the deck.")
			else:
				currentPlayer.addCardToHand(dealtCard)
		else:
			print(selectedPlayer.name + " has " + str(selectedPlayer.countNumValue(requestedValue)) + " " + requestedValue + "s.")
			takenCards = [card for card in selectedPlayer.hand if card.value == requestedValue]
			for card in takenCards:
				selectedPlayer.removeCardInHand(card)
				currentPlayer.addCardToHand(card)
		
		for player in goFish.players:
			if len(player.hand) == 0:
				print(player.name + " has no more cards in their hand.")
				books = player.getBooks()
				for book in books:
					print("\n" + player.name + " has acquired four of " + book + "s!")
				goFish.players.remove(player)
				if len(goFish.players) == 1:
					print(goFish.players[0].name + " won the game!")
					return 0
	
		goFish.advancePlayer()

if __name__ == "__main__":
	main()