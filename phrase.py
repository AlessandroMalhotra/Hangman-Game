
class Phrase:

	def __init__(self, phrase):
		self.phrase = phrase.lower()


	# Displays the letter location in the phrase on screen,
	# If the user inputs a letter that is in the phrase
	def display(self, guesses):

		for letter in self.phrase:
			if letter in guesses:
				print(f'{letter}', end=' ')
			else:
				print('_', end=' ')

	# Checks if user input is not a letter and asks them to try again
	def check_guess(self, guess):
		if len(guess) > 1 or guess.isalpha() == False:
			print("This is not a valid entry. Try again.")
			return False
		return guess in self.phrase

	
	# Checks if user has already gusssed a letter 
	def check_complete(self, guesses):
		for letter in self.phrase:
			if letter not in guesses:
				return False
		return True

