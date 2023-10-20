print('Welcome to my computer game')
quest = input('Do you want to play? ')

if quest.lower() != "yes":
    quit()
print("Okay! let's play")
score = 0
first_question = input('What does CPU stand for ')
if first_question.lower() == 'central processing unit':
    print('Correct answer!')
    score += 1
else:
    print('wrong answer')
    
second_question = input('Where do you stay? ')
if second_question.lower() == 'ashaiman':
    print('Correct answer!')
    score += 1
else:
    print('wrong answer')
    
third_question = input('Name of your school ')
if third_question.lower() == 'all nations':
    print('Correct answer!')
    score += 1
else:
    print('wrong answer')

fourth_question = input('Do you love me? ')
if fourth_question.lower() == 'yes':
    print('Correct answer!')
    score += 1
else:
    print('wrong answer')
if score == 4:
    print(f"Overall percentage = {score / 4 * 100 }% \n 'Congratulation! on winning your first price :)'")
else:
    print("Sorry, You failed. Try agian")