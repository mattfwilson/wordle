# check to see if two of the same character is in the guess
# stacking the result summary (needs list of lists - Andres)

wordle = 'plebs'
userInput = ''
guess = ''
gameContinue = True
guessCount = 0 

def checkGuess(guess, word, outputGuess, count):
    guess_index = 0

    while guess_index < len(guess): # check if guess letter exists in word at all
        guessLetter = guess[guess_index]
        if guessLetter in word:
            outputGuess[guess_index] = '(' + guess[guess_index] + ')'
        guess_index += 1

    word_index = 0
    correctCount = 0
    while word_index < len(word): # check if position of letter match
        wordLetterPos = word[word_index]
        guessLetterPos = guess[word_index]
        if guessLetterPos == wordLetterPos:
            outputGuess[word_index] = '[' + guess[word_index] + ']'
            correctCount += 1
        word_index += 1
    print(f'Result: {outputGuess}')
    count += 1
    return correctCount != len(word)

while gameContinue == True:
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
