# Hangman game with command line (Simple version)

# Pseudo code for the task
# 1. loop max. turn count of 6 (6 is the live )
    # 2. Get a guess
    # 3. check if the guess is in the secrect word
        #4. if wrong decrease the live by one
        # 5. if true, print the correct letters
    # if all the letters are correct, break out of the loop
    

# initializing the secret word of the game
secret_word = "Computer".upper()
# initialize the live count
lives = 6
# initialize the used letters
guessed_letters = ""

def hangman1():
    # loop that runs until the user guess everything correctly
    while lives > 0:
        # get the guess letter
        guess = input("Guess the correct letter:  ").upper()

        # check if the guess input is in the secret word
        if guess in secret_word:
            # Player guessed correctly
            print(f"correct, there is one or more {guess} in the secret word")  
        else:
            # decrease the live and print info to user
            lives -= 1
            print(f"incorrect, there is no {guess} in the secret word and lives remain {lives} to finish")
        
        # maintain a list of all the guessed letters
        guessed_letters += guess
        wrong_letter_count = 0
        # logic that check if the user guessed all the letters
        for letter in secret_word:
            if letter in guessed_letters:
                print(f"{letter} ", end="")
            else:
                print(" - ", end=" ")
                wrong_letter_count += 1
        
        # check if the wrong letter count is still zero
        if wrong_letter_count == 0:
            print(f"Congratulations!!, The secret was: {secret_word}. You won")
            break
     
     
     
     
# intermediate version

# import random for choosing different words
import random 
# import words from words.py
from words import words
import string

# get valid word function
def get_valid_word(words):
    # randomly choose a word from the list
    word = random.choice(words)
    # check for special characters in words
    while '-' in words or ' ' in words:
        word = random.choice(words)

    return word.upper()

def hangman2():
    # initaializing the word to guess from and guessed word and lives
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6
    wrong_count_letter = 0
    
    while lives > 0 and len(word_letters) > 0:
        # print to the user letters used
        print("You have used: ", ' '.join(used_letters))
        
        # what current word is 
        # for letters in word:
        #     if letters in used_letters:
        #         print(f'{letters}', end='')
        #     else:
        #         print(' - ', end='')   
        
                # OR        
                
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ", ' '.join(word_list))   
             
        # getting user input
        user_letter = input('Guess a letter: ').upper()
        # check if the letter is in secret word
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                # decrease the live
                lives -= 1
                if lives != 0:
                    # letter not in the word 
                    print('Letter not in the word and lives remaining {}, Try again'.format(lives))
                
                
                
        elif user_letter in used_letters:
            print("You have already guess this letter, try again")
        else:
            print("invalid character, try again")

    if lives == 0:
        print("Your life has Exhausted, Please start from the beginning")
    else:
        print('You Guessed the word ', word)
    
hangman2()