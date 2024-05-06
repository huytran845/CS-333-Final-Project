#Author: Huy Tran
#CS 333 Testing Dev Ops
#5/7/2024

from gofish import GoFish

def main():
	while True:
		try:
			numPlayers = int(input("How many people are playing? "))
			while numPlayers <= 0 or numPlayers == 1:
				print("Invalid number of players, please try again!")
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

		currentBooks = currentPlayer.getBooks()
		for book in currentBooks:
			print("\n" + currentPlayer.name + " has acquired four of " + book + "s!")
			for player in goFish.players:
				if player == currentPlayer:
					player.removeSameCards(book)
					player.totalBooks += 1
					goFish.books += 1
		
		if goFish.books == 13:
			break

		print("\nCards in " + currentPlayer.name + "'s hand:")
		for card in currentPlayer.hand:
			print(card)
		
		requestedValue = input("\n" + currentPlayer.name + ", what card value would you like to ask for? Ace, 2-10, Jack-King: ")
		currentValues = [card.value for card in currentPlayer.hand]
		if not requestedValue in GoFish.values:
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
			if len(player.hand) == 0 and len(goFish.startDeck) == 0:
				print(player.name + " has no more cards in their hand and is unable to draw.")
				books = player.getBooks()
				for book in books:
					print("\n" + player.name + " has acquired four of " + book + "s!")
				goFish.finishPlayers(player)
	
		goFish.advancePlayer()

	winner = goFish.removedPlayers[0]
	for player in goFish.removedPlayers.copy():
		if player.totalBooks > winner.totalBooks:
			winner = player
	
	print(winner.name + " has won the game with " + str(winner.totalBooks) + " books!")

if __name__ == "__main__":
	main()