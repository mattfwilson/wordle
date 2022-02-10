# check to see if two of the same character is in the guess
# stacking the result summary (needs list of lists -Andres)

wordle = 'plebs'
userInput = ''
guess = ''
gameContinue = True
guessCount = 1

def checkGuess(guess, word, outputGuess, count):
    guess_index = 0
    word_index = 0
    correctCount = 0

    while guess_index < len(guess):                 # create var with list character/index for guess
        guessLetter = guess[guess_index]
        if guessLetter in word:                     # check to see a guess character in the wordle
            outputGuess[guess_index] = '(' + guess[guess_index] + ')'
        guess_index += 1

    while word_index < len(word):                   # create vars with list characters/index for guess AND wordle
        wordLetterPos = word[word_index]
        guessLetterPos = guess[word_index]
        if guessLetterPos == wordLetterPos:         # check if positions of guess characters and wordle characters matche
            outputGuess[word_index] = '[' + guess[word_index] + ']'
            correctCount += 1
        word_index += 1
    print(f'Result: {outputGuess}')
    count += 1
    return correctCount != len(word)

while gameContinue == True:                         # keeps game running while user still has guesses
    if guessCount <= 6:
        guess = input('What is your first guess? ')
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
        print('You are out of turns. Game over.')
        quit()
