from simplestack import Stack
from random import randint

class Hangman():
	def __init__(self):
		print "*** HANGMAN ***"
		print "Ready to play, criminal?"
		print "(1)Yes\n(2)No"
		choice = raw_input("-> ")
		
		if choice == '1':
			print "Game is LOADING criminals!"
			self.start_game()
		elif choice == '2':
			print "Good Bye Criminal!"
			exit()
		else:
			print "Wrong Choice, criminal!"
			self.__init__()

	def play_again(self):
		print "You were lucky to escape. You Win!"		
		again = input("Do you want to play again?\n(1)Yes\n(2)No\n-> ")

		if again == 1:
			print 
			self.start_game()
		elif again == 2:
			print "Good Bye Criminal!"
			exit()
		else: 
			print "Wrong Choice!\n Choose again.\n"
			self.play_again()

	def start_game(self):
		print 
		print "Let's get started. Get ready to be HANGED!"
		print
		self.main_game()

	def main_game(self):
		guesses = 0
		letters_used = ""
		words = ['aisle', 'zebra', 'waste', 'vocal', 'stand', 'quiet', 'night', 'light', 'heart', 'active', 'advent', 'alumni', 'garden', 'german', 'grapes', 'stupid', 'scream', 'dancer', 'darkest', 'dolphin', 'rainbow', 'rectify', 'python', 'codes', 'zealous', 'backlog']
		word_rand = randint(1, len(words))
		the_word = words[word_rand]
		progress = self.get_progress(the_word)
		prog_u = ""

		s = Stack()
		t = Stack()
		
		for x in xrange(len(the_word)):
			t.push(the_word[x])
		print "Number of letters:", t.size()

		while guesses < 6 :
			guess = raw_input("Guess a letter -> ")
			if guess in the_word and not guess in letters_used:
				print "As it turns out, your guess was RIGHT!"
				letters_used += "," + guess
				self.hangman_graphic(guesses, the_word)
				prog_u = self.proper_progress(guess, the_word, progress)
				s.push(prog_u)
				print "Progress: " + prog_u
				print "Letters used: " + letters_used

				while s.top == "_ ":
					s.pop()
				print s.size()
				if s.size() == t.size():
					print
					self.play_again()

					
			elif guess not in the_word and not guess in letters_used:
				guesses += 1
				print "Things aren't looking so good, that guess was WRONG!" 
				letters_used += "," + guess
				self.hangman_graphic(guesses, the_word)
				print "Progress: " + "".join(progress)
				print "Letter used: " + letters_used

			else:
				print "That's the wrong letter"
				print "Try again!"


	def get_progress(self, the_word):
		progress_stack = Stack()
		if len(the_word) == 5:
			return ["_ ", "_ ", "_ ", "_ ", "_ "]
		elif len(the_word) == 6:
			return ["_ ", "_ ", "_ ", "_ ", "_ ", "_ "]
		elif len(the_word) == 7:
			return ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "]
	
	def proper_progress(self, guess, the_word, progress):
		i = 0
		while i < len(the_word):
			if guess == the_word[i]:
				progress[i] = guess
				i += 1
			else:
				i += 1

		return ''.join(progress)

	def hangman_graphic(self, guesses, the_word):
		if guesses == 0:
			print "________      "
			print "|      |      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 1:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 2:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /       "
			print "|             "
			print "|             "
		elif guesses == 3:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|      "
			print "|             "
			print "|             "
		elif guesses == 4:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|             "
			print "|             "
		elif guesses == 5:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     /       "
			print "|             "
		else:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     / \     "
			print "|             "
			print "The word was: " + the_word
			print
			print "GAME OVER!"
			print
			self.__init__()

play = Hangman()



