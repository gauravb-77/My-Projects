import random
total_number_of_games = 1
comp_score = 0
user_score = 0
while total_number_of_games <= 9:
    print(
        'Welcome to Snake, Water and Gun game! Let\'s play it')
    comp_choice = random.choice(['Snake', 'Water', 'Gun'])
    user_choice = input(
        'Enter your choice between Snake(s), Water(w) and Gun(g):\n')
    print(f"Computer's choice: {comp_choice}")
    if comp_choice == 'Snake' and user_choice.lower() == 'w':
        comp_score += 1
        print(
            f'Computer won this game\ncomp_score = {comp_score}\nuser_score = {user_score}\n')
    elif comp_choice == 'Water' and user_choice.lower() == 's':
        user_score += 1
        print(
            f'You won this game\ncomp_score = {comp_score}\nuser_score = {user_score}\n')
    elif comp_choice == 'Snake' and user_choice.lower() == 'g':
        user_score += 1
        print(
            f'You won this game\ncomp_score = {comp_score}\nuser_score = {user_score}\n')
    elif comp_choice == 'Gun' and user_choice.lower() == 's':
        comp_score += 1
        print(
            f'Computer won this game\ncomp_score = {comp_score}\nuser_score = {user_score}\n')
    elif comp_choice == 'Water' and user_choice.lower() == 'g':
        comp_score += 1
        print(
            f'Computer won this game\ncomp_score = {comp_score}\nuser_score = {user_score}\n')
    elif comp_choice == 'Gun' and user_choice.lower() == 'w':
        user_score += 1
        print(
            f'You won this game\ncomp_score = {comp_score}\nuser_score = {user_score}\n')
    else:
        total_number_of_games -= 1
        print(f'Tie\ncomp_score = {comp_score}\nuser_score = {user_score}\n')
    total_number_of_games += 1
print(f"Computer's total score: {comp_score}\nYour total score: {user_score}")
if comp_score > user_score:
    print('Computer won the game!!')
else:
    print('You won the game!!')





