# This is an On-Screen Master Mind Game

# Import random library
import random

# Insturction
def instructions():
    print("\n1. I'll pick four random colours from the colours provided to form a sequence.")
    print("2. Then, you'll need to guess the colours in the exact positions")
    print("   in the sequence I formed.")
    print('3. Same colour can be selected for more than once randomly.')
    print('4. For each of your guess,')
    print("   hints like how many 'correct colour is in correct position' and")
    print("   how many 'correct colour is NOT in the correct position' in the code sequence")
    print("   will be shown.")
    print("5. You win the game when you manage to guess all the colours")
    print("   in the code sequence and they are all in the right position.")
    print('6. PS: You only have 15 GUESSES')
          
# Welcome Message
print()
print('----------- Welcome to On-Screen Master Mind Game! -----------')
print()

# Colours to be randomized
colourlist = ['Y', 'B', 'W', 'R']

# Input player name and choose if they need instructions
player = input('Please Enter Player Name: ')
needhelp = input('\nFirst time playing? \nEnter "Y" for instructions! or enter "N" to start the game\n: ')

# Instruction Request
if needhelp == 'Y' or needhelp == 'y':
    instructions()

start = input("\nLet's start, shall we? \n\nPress Enter to Start!")
print("\n" + player + ':' " Let's rock and roll !!!")
    
# Instruction of repeating the game 
repeat = 'Y'
while repeat == 'Y' or repeat == 'y':

# Game Guide
    print()
    print('Try to guess the four mysterious colours using the colours provided! \n\nEnter the colours by using the first letter of the colour. \nExp: Y for Yellow')
    print('Colours provided: YELLOW (Y), BLACK (B), WHITE (W), RED (R)')
    print()
    print('You only have 15 chances so goodluck!!!')
    print()

# Random Colours Generator
    def ColoursGenerated(colourlist):
        ColoursGenerated = []
        for i in range(4): 
            ColoursGenerated.append(random.choice(colourlist)) 
        return ColoursGenerated

    Answer = ColoursGenerated(colourlist)

# Initialize user's input, no. of guesses, no. of correct and wrong guesses
    colours_chosen = []
    Guesses = 0
    correct = 0
    wrong = 0

# Loop of inputs
    while correct < 4:
        if Guesses >= 15:
            print('Opps! You have reached the maximum attempts. \nYou lose! Try again next time!')
            repeat = input('\nWanna play again? [Y/N]\n:')
        else:
            Guesses += 1
            while len(colours_chosen) < 4:
                attempt = str(input('Please choose a colour: ').upper())
                if attempt not in colourlist:
                    print('Error: Please choose the colours from the colour list provided, Thank You.')
                else:
                    colours_chosen.append(attempt)

            print('Colours Chosen:',colours_chosen)

            # Answer checking
            if correct != 4:
                    for i in range(4):                       
                            if colours_chosen[i] == Answer[i]:
                                correct += 1
                                colours_chosen[i] += 'a'
                                Answer[i] += 'a'
                                
                    for i in range(4):
                            if colours_chosen[i] != Answer[i] and colours_chosen[i] in Answer:
                                wrong += 1
                                Answer[Answer.index(colours_chosen[i])] += 'a'
                                
                    for i in range (4):
                            if len(Answer[i]) > 1:
                                Answer[i] = (Answer[i])[0]
                                                                                   
            # Results
            if correct < 4:
                print('\nCorrect colour in the correct place: ' + str(correct))
                print('Correct colour in the wrong place: ' + str(wrong) + '\n\nTry harder! You can do it!!!\n')
                correct = 0
                wrong = 0
                colours_chosen = []
                continue
            else:
                if Guesses == 1:
                    print('Congratulations, ' + player + '! You are the best !!! \n ---It took you only ' + str(Guesses) + ' guess!---')
                else:
                    print('Congratulations, ' + player + '! You made it !!! \n ---It took you only ' + str(Guesses) + ' guesses!---')

            repeat = input('\nWanna play again? [Y/N]\n:')

# End of Program      
        break
print('\nThank you for playing, hope you like this game! \nSee you next time! Bye~')
