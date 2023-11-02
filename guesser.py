import getpass


def output(entry, pos):
	print(f"{''.join(entry)} ({pos})")

def game():
	word = 'smth'
	while word != '':
		word = getpass.getpass('Enter your word to start game: ')
		letters = []
		sign = ' _ '
		cipher = []
		counter = 0

		for letter in word:
			letters.insert(0, letter)

		letters.reverse()

		for i in range(0, len(letters)):
			cipher.insert(0, sign)

		output(cipher, len(letters))

		while counter != 3:
			answer = input('Try to guess the letter: ')

			if answer in letters:
				
				for i in range(0, len(letters)):
					if letters[i] == answer:
						position = i

				position_output = position + 1

				cipher[position] = answer

				output(cipher, position_output)
			
			else:
				counter += 1
				print('Wrong letter')
				word = ''

			if counter == 3:
				print('''
\033[0;31;47m Game over \033[0m
					''')

			if sign not in cipher:
				print('''
\033[0;32;47m You win! \033[0m
					''')
				counter = 3
				word = ''

game()


while True:
	replay = input('Do you want to play again?: ')
	if replay == 'yes':
		game()
	else:
		break

