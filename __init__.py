if play_again.lower() == 'yes':
    self.guesses = [' ']
    self.missed = 0
    aelf.active_phrase = random.choice(self.phrasees)
    return self.start()
else:
    print("\nThank you for playing, Goodbye!")