"""
To-dos
check to see if two of the same character is in the guess
stacking the result summary (needs list of lists -Andres)
Add in conditional check for if the guess word is < or > 5 characters
"""

from PyDictionary import PyDictionary
import random
import pickle

lookup = PyDictionary()
wordle = ''
userInput = ''
guess = 'guess'
gameContinue = True
guessCount = 1
record = {'wins': 0, 'losses': 0}

def checkGuess(guess, word, outputGuess, count):
    global guessCount
    guess_index = 0
    word_index = 0
    correctCount = 0

    while guess_index < len(guess): # create var with list character/index for guess
        guessLetter = guess[guess_index]
        if guessLetter in word: # check to see a guess character in the wordle
            outputGuess[guess_index] = '(' + guess[guess_index] + ')'
        guess_index += 1
    while word_index < len(word): # create vars with list characters/index for guess AND wordle
        wordLetterPos = word[word_index]
        guessLetterPos = guess[word_index]
        if guessLetterPos == wordLetterPos: # check if positions of guess characters and wordle characters match
            outputGuess[word_index] = '[' + guess[word_index] + ']'
            correctCount += 1
        word_index += 1
    print(f'Guess {guessCount}: {outputGuess}')
    guessCount += 1
    return correctCount != len(word)


record = pickle.load(open('user_record.dat', 'rb'))
print(f'Wins: {record["wins"]} | Losses: {record["losses"]}')

with open("test_words.txt", "r") as possibleWords: # get/create list out of 5-letter-words.txt
        file_lines = possibleWords.read()
        wordList = file_lines.split("\n")

wordle = random.choice(wordList)

while gameContinue == True: # keeps game running while user still has guesses
    if guessCount <= 6:
        while len(guess) < 5 or len(guess) > 5: # checks to make sure the guess is 5 characters long
            print(f'Your guess word has to be five characters.')
            guess = input(f'What is your guess? ({guessCount}/6) ')

        guess = input(f'What is your guess? ({guessCount}/6) ')
        word_char = []
        guess_char = []
        output_lst = []
        for character in guess:
            guess_char.append(character)
            output_lst.append(character)

        for character in wordle:
            word_char.append(character)

        gameContinue = checkGuess(guess_char, word_char, output_lst, guessCount)

        if gameContinue == False:
            print(f'You won! You figured out the word was "{wordle}"!')
            record["wins"] += 1
            pickle.dump(record, open('user_record.dat', 'wb'))
            print(f'Wins: {record["wins"]} | Losses: {record["losses"]}')
            quit()
    elif guessCount > 6:
        print(f'Game over! You used all 6 guesses. The correct word was "{wordle}"!')
        record["losses"] += 1
        pickle.dump(record, open('user_record.dat', 'wb'))
        print(f'Wins: {record["wins"]} | Losses: {record["losses"]}')
        quit()
