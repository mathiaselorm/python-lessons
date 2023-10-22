import random 
 
highest_number = input('Type a number: ')
if highest_number.isdigit():
    highest_number = int(highest_number)
    
    if highest_number <= 0:
        print('Type a number greater than zero!')
        quit()
else:
     print('please type a number')
     quit()
    
random_number  = random.randint(0, highest_number)

guess = 0
while True:
    guess += 1
    guess_number = input(' Guess a number: ')
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print('please type a number')
        continue
    if guess_number == random_number:
        print('You got it!')
        break
    elif guess_number > random_number:
            print('Your guess is above the number')
    else:
            print('Your guess is below the number')
    if guess == 5:
        print('Sorry, you run out of guesses! \n Try again')
        quit()
print(f"You got it in {guess} guesses")