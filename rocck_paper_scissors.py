import random

options = ['rock', 'paper', 'scissors']
user_wins = 0
Computer_wins = 0

while True:
    user_input = input("Rock/ Paper/ Scissors or 'q' to quit: ").lower()
    if user_input == 'q':
        break
    
    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    
    computer_pick = options[random_number]
    print(f"computer picked {computer_pick}.")

    if user_input not in options:
        print(f"Please enter Rock/ Paper/ Scissors or 'q' to quit.")
        continue

    elif user_input == 'rock' and computer_pick == 'paper':
        print('You Won!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'rock':
        print('You Won!')  
        user_wins += 1     
    elif user_input == 'paper' and computer_pick == 'scissors':
        print('You Won!')
        user_wins += 1
    else:
        print('You Lost!')
        Computer_wins += 1
print(f"You won {user_wins} times.")
print(f"Computer won {Computer_wins} times.")
print('Goodbye!')