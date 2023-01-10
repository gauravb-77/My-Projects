
comp_num = 24
print('Welcome to The Number Guessing Game! In this game you have 9 guesses. So let\'s play the game.')
i = 1
while i <= 9:
    num = int(input('Enter a number:\n'))
    if i < 9:
        if num < comp_num:
            print('\nPlease increase your number\nYour no. of guesses left:', 9 - i)
        elif num > comp_num:
            print('\nPlease decrease your number\nYour no. of guesses left:', 9 - i)
        else:
            print('\nYou Won!\nYou took', i, 'guesses for this')
            break
    else:
        if num == comp_num:
            print('\nYou Won!\nYou took', i, 'guesses for this')
        else:
            print('\nGame Over!')
    i = i + 1
