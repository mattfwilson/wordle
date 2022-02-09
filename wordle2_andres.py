# check to see if two of the same character is in the guess
# stacking the result summary (needs list of lists - Andres)

word = 'digit'
user_input = ''
result = None
guess = 'dggnt'
gameOn = True

def letter_in_word(guess, word, outputGuess):
    index2 = 0

    while index2 < len(guess): # check if guess letter exists in word at all
        guessLetter = guess[index2]
        if guessLetter in word:
            print(f'{guessLetter} is in the word')
            outputGuess[index2] = '(' + guess[index2] + ')'
        index2 += 1

    index = 0
    correctCount = 0
    while index < len(word): # check if position of letter match
        wordLetterPos = word[index]
        guessLetterPos = guess[index]
        if guessLetterPos == wordLetterPos:
            outputGuess[index] = '[' + guess[index] + ']'
            correctCount += 1
        index += 1
    print(outputGuess)
    return correctCount != len(word)


while gameOn == True:
    guess = input('What is your first guess? ')
    word_char = []
    guess_char = []
    output_lst = []

    for character in guess:
        guess_char.append(character)
        output_lst.append(character)
    print(f'Your guess: {guess_char}')

    for character in word:
        word_char.append(character)
    print(f'The word: {word_char}')

    gameOn = letter_in_word(guess_char, word_char, output_lst)

# exactMatch = [index for index, (guess_letter, word_letter) in enumerate(zip(guess_char, word_char)) if guess_letter == word_letter]
# print(exactMatch)

# if guess_char[0] == word_char[0]:
#     print(f'Match!')
# if guess_char[1] == word_char[1]:
#     print(f'Match!')
# if guess_char[2] == word_char[2]:
#     print(f'Match!')
# if guess_char[3] == word_char[3]:
#     print(f'Match!')
# if guess_char[4] == word_char[4]:
#     print(f'Match!')

###########################

# for character in guess:
#     guess_char.append(character)

# for character in word:
#     word_char.append(character)

# print(word_char)
# print(guess_char)

# for i in guess_char:
#     if i in word_char:
#         print(f'{i} is in the word!')

###########################

# for letter in word:
#     pos = word.find(letter)6
#     word_check.append(pos)
# print(word_check)

# for letter in guess:
#     if letter in word:
#         pos = word.find(letter)
#         guess_check.append(pos)

# print(guess_check)
# i
# for match in guess_check:
#     if match == word.find(str(match)):
#         word.replace(match, '*')

# print(word)

###########################

# for x in range(0, len(guess1)):
#     breakldgjt

# for i in range(0, len(word)):
#     if word[i] == guess1:
#         result = i + 1
#         break

# if result == None:
#     print ("No such character available in string")
# else:
#     print ("Character {} is present at location {}".format(guess1, str(result)))
    