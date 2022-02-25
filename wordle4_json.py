# To-dos
# check to see if two of the same character is in the GUESS
# stacking the result summary (needs list of lists -Andres)
# conditional check for < or > 5 characters not working after first guess

import random
import json

WORDLE = ''
GUESS = ''
CONTINUE = True
GUESS_COUNT = 1
RECORD = {}

# function to validate guesses and outputs results
def check_guess(guess, word, output_guess):
    global GUESS_COUNT
    guess_index = 0
    word_index = 0
    correct_count = 0

    # create var with list character/index for guess
    while guess_index < len(guess):
        guess_letter = guess[guess_index]
        # check to see a GUESS character in the wordle
        if guess_letter in word:
            output_guess[guess_index] = '(' + guess[guess_index] + ')'
        guess_index += 1
    # create vars with list characters/index for guess AND wordle
    while word_index < len(word):
        word_letter_pos = word[word_index]
        guess_letter_pos = guess[word_index]
        # check if positions of GUESS characters and wordle characters match
        if guess_letter_pos == word_letter_pos:
            output_guess[word_index] = '[' + guess[word_index] + ']'
            correct_count += 1
        word_index += 1
    print(f'Guess {GUESS_COUNT}: {output_guess}')
    GUESS_COUNT += 1
    return correct_count != len(word) # this equals False if all letters are not correct


# loads historical record from external json file
with open('records.json', 'r') as save:
     RECORD = json.load(save)
print(f'Wins: {RECORD["wins"]} | Losses: {RECORD["losses"]}')

# loads external words list and randomly selects word from it
with open("test_words.txt", "r") as possible_words: # get/create list out of 5-letter-words.txt
        file_lines = possible_words.read()
        word_list = file_lines.split("\n")
        WORDLE = random.choice(word_list)

# continue running game while user still has available guesses
while CONTINUE == True:
    if GUESS_COUNT <= 6:
        # checks to make sure the GUESS is 5 characters long
        if len(GUESS) < 5 or len(GUESS) > 5:
            print(f'Your guess word has to be five characters. haha')
            GUESS = input(f'What is your GUESS? ({GUESS_COUNT}/6) ')
        elif len(GUESS) > 5:
            print(f'Your GUESS word has to be five characters.')
            GUESS = input(f'What is your guess? ({GUESS_COUNT}/6) ')
        else:
            GUESS = input(f'What is your guess? ({GUESS_COUNT}/6) ')
        
            word_char = []
            guess_char = []
            output_lst = []

            for char in GUESS:
                guess_char.append(char)
                output_lst.append(char)
            for char in WORDLE:
                word_char.append(char)

            CONTINUE = check_guess(guess_char, word_char, output_lst)
            print(CONTINUE)
            if CONTINUE == False:
                print(f'You won! You figured out the word was "{WORDLE}"!')
                RECORD["wins"] += 1
                with open('records.json', 'w') as save:
                    json.dump(RECORD, save)
                print(f'Wins: {RECORD["wins"]} | Losses: {RECORD["losses"]}')
                quit()
    elif GUESS_COUNT > 6:
        print(f'Game over! You used all 6 guesses. The correct word was "{WORDLE}"!')
        RECORD['losses'] += 1
        with open('records.json', 'w') as save:
            json.dump(RECORD, save)
        print(f'Wins: {RECORD["wins"]} | Losses: {RECORD["losses"]}')
        quit()