import random
# # HANGMAN!
# # 1. Make a program that selects a word from a list of words
# # 2. From each category, select a random word
# # 3. Accept user input that asks the user to type in a category
# ​# randomly_selected_word = "orange"
# ​# 4. _ _ _ _ _ _
# ​# 5. if you make a correct choice = "o" => o _ _ _ _ _
# ​# randomly_selected_word = "watermelon"
# # 6. _ _ _ _ _ _ _ _ _ _ _
# # 7. if you make a correct choice = "e" => _ _ _ e _ _ e _ _ _
# # 8. 7 attempts
# # 9. if you exhause all 7 choices, show the correct word


class WordBank:
	"""Bank of words to choose from"""
	wordbank = {
		"food": ["pizza", "stromboli", "pasta"],
		"animals": ["cat", "dog", "mouse"],
		"space": ["moon", "earth", "jupiter"]
	}

	def get_word(self, key):
		return HiddenWord(random.choice(self.wordbank[key]))

class HiddenWord:
	"""Show dashes to reveal how many letters, replace dashes with correct letter"""
	def __init__(self, random_word):
		self.word = random_word

	def __str__(self):
		return f'The hidden word was {self.word}'
		
	def dash_maker(self):
		for i in self.word:
			print("_", end=" ")
			# print(i, end=" ")
		print("\n")

class GuessWord:
	"""Reveal correctly guessed letters"""
	
	
class Game:

	@classmethod
	def run(self):

		print("welcome".upper())
		active = True
		while active:
			
			choice = input("choose category: 'food', 'animals', 'space': ")
			words = WordBank()
			random_word = words.get_word(choice)
			random_word.dash_maker()

			guess = []
			tries = 7
			game_over = False
		
			while not game_over:
				guess_letter = input("Enter a letter to guess.  You have " + str(tries) + " tries left: ".lower())			
				if guess_letter in random_word.word: 
					guess.append(guess_letter)
					game_won = True
					for i in random_word.word:
						if i not in guess:
							game_won = False
					print("you guessed right!".upper())
					if game_won == True:
						print("** you won **".upper())
						game_over = True
						confirmation = input("keep playing? (y/n) ".lower())
						if confirmation[0] == "n":
								print("thanks for playing")
								break
						else:
							confirmation == "y"
							active = True
							break

				else:
					tries -= 1
					if tries == 0:
						print("I'm sorry, you did not guess the word!")
						print(random_word)
						game_over = True
						confirmation = input("keep playing? (y/n) ".lower())
						if confirmation[0] == "n":
							print("thanks for playing")
							game_over = True
						else:
							confirmation == "y"
							active = True
							break
				
				for i in random_word.word:
					if i in guess:
						print(f' {i} ', end="")
					elif guess_letter != i in random_word.word:
						print(f"_ ", end="")
				

				
			else:
				confirmation == "n"
				active = False
				



Game.run()
	