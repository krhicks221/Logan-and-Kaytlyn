def numberseven():
	import random

	def play_again():
		while True:
			replay = input('Play again? Yes or No?\n')
			if replay.lower() == 'yes':
				return True
			elif replay.lower() == 'no':
				return False
			print('Invalid input.')

	def main():
		print('Welcome to the number guess game!', end='\n\n')

		random_number = random.choice(range(1, 401))

		print("I'm thinking of a number between 1 and 400 (good luck). Can you guess it?")

		guesses, guess = 0, 0

		while guess != random_number:
			try:
				guess = int(input("Enter a number: "))
			except:
				print('Invalid input.')
				continue
			if guess > random_number:
				print('Too high. Guess lower.')
			elif guess < random_number:
				print('Too low. Guess higher.')
			guesses+=1
		print('Congratulations. You guessed my number {0} in {1} guesses'.format(random_number, guesses))

		if play_again():
			main()
		else:
			print('Hasta la vista, baby!')

	main()
