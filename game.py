import random

def playAgain():
    answer = input("Would you like to play the game again? yes/no: ").lower()
    if answer == "y" or "yes":
        playGame()
    else:
        pass

def getWord():
    
    words = ["car", "pizza", "orange", "animal", "basketball", "hockey", "sports"]
    return random.choice(words)


def playGame():
    alphabet = "abcdefghijklmnopqrstuvwxyzæøå"
    word = getWord()
    letters_guessed = []
    tries = 6
    guessed = False

    print("The word contains", len(word), 'letters') 
    print(len(word) * '*')
    while guessed == False and tries > 0:
        print("You have " + str(tries) + " tries.")
        guess = input("Please enter one letter or the full word: ").lower() 
        #1 - user inputs a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print("You have not entered a letter")
            elif guess in letters_guessed:
                print("You have already guesssed that letter before.")
            elif guess not in word:
                print("Sorry, that letter is not part of the word.")
                letters_guessed.append(guess)
                tries -= 1
            elif guess in word:
                print("Well done, that letter exists in the word")
                letters_guessed.append(guess)
            else:
                print("Error, let us investigate the issue!")

        #2 - user inputs the full word
        elif len(guess) == len(word):
            if guess == word:
                print("Well done, you have guessed right!")
                guessed = True
            else:
                print("Sorry, this is not the word we are looking for")
                tries -=1



        #3 - user inputs letters where the total number of letters =/= total number of letters in the word
        else:
            print("The length of your guess is not the same as the length of the word we are looking for.")
            
        
        status = '' #user status update
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += "*"
            print(status)

            if status == word:
                print("Well done, you have guessed the right word!")
                guessed == True
            elif tries == 0:
                print("You have run out of guesses and you haven\'t guessed the word.")
        
    playAgain() 

playGame() 
