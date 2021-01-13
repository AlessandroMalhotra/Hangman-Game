
from phrase import Phrase
import random

class Game:

	def __init__(self):
		self.missed = 0
		self.phrases = [Phrase('life is like a box of chocolates'), Phrase('luke i am your father'), Phrase('live every day like it is your last'), Phrase('a piece of cake'), Phrase('speak of the devil')]
		self.active_phrase = self.get_random_phrase()
		self.guesses = [' ']

	
	def get_random_phrase(self):
		
		for phrase in self.phrases:
			random_phrase = random.choice(self.phrases)
		return random_phrase

	
	def welcome(self):
		welcome_message = """
		======================================
		  Welcome to the Phrase-Hunter Game!
		======================================
		"""
		print(welcome_message)


	def start(self):
		self.welcome()
		while (self.missed < 5 and not self.active_phrase.check_complete(self.guesses)):
			print(f'Number missed: {self.missed}')
			self.active_phrase.display(self.guesses)
			user_guess = self.get_guess()
			self.guesses.append(user_guess)
			
			if not self.active_phrase.check_guess(user_guess):
				self.missed += 1
		self.game_over()


	def get_guess(self):
		self.guess = input('\n\nEnter a letter: ')
		return self.guess


	def game_over(self):
		if self.missed == 5:
			print('You lost!')
		else:
			print('Congratulations you won!')


	def play_again(self):
		play_again = input("\nGame Over! Would you like to play again Yes/No: ")

		if play_again.lower() == 'yes':
			self.guesses = [' ']
			self.missed = 0
			self.active_phrase = random.choice(self.phrases)
			return self.start()
		else:
			print("\nThank you for playing, Goodbye!")
      


