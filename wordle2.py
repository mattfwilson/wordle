# check to see if two of the same character is in the guess
# stacking the result summary (needs list of lists -Andres)
# Add in conditional check for if the guess word is < or > 5 characters

# from PyDictionary import PyDictionary

# lookup = PyDictionary()
wordle = 'sushi'
userInput = ''
guess = 'guess'
gameContinue = True
guessCount = 1
counter = 0

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
            counter += 1
        word_index += 1
    print(f'Guess {guessCount}: {outputGuess}')
    guessCount += 1
    return correctCount != len(word)

while gameContinue == True: # keeps game running while user still has guesses
    if guessCount <= 6:
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
    elif guessCount > 6:
        print(f'Game over! You used all 6 guesses. The word was "{wordle}"!')
        # dictResult = lookup.meaning(f'{wordle}')
        # print(f'Defintion of {wordle}: \n{dictResult}')
        quit()
