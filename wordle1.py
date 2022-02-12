word = 'light'
user_input = ''
result = None
guess = 'hitgt'
guess = 'hztgo'

# guess = input('What is your first guess? ')

guess_char = []
word_char = []
new_lst = []

###########################

for character in guess:
    word_char.append(character)
print(f'The word: {word_char}')


exactMatch = [index for index, (guess_letter, word_letter) in enumerate(zip(guess_char, word_char)) if guess_letter == word_letter]
print(f'Exact match indices: {exactMatch}')

new_string = ''

for match in exactMatch:
    guess_char.append(match)
    print(guess_char)


# for i in guess_char:
#     if i in word_char:
#         nonMatchIndex = guess_char.index(i)
#         print(f'Non-matching letters: {i}')
# print(f'Non-matching letters: {nonMatchIndex}')

# results = [index for index, (guess_letter, word_letter) in enumerate(zip(guess_char, word_char)) if guess_letter != word_letter]
# print(f'Non-matching indices: {results}')

def letter_in_word(guess, word):
    for i in guess:
        if i in word:
            print(f'{i} is in the word')
        else:
            print(f'{i} is not in the word')

for i in guess_char:
    if i in word_char:
        print(f'{i} is in the word')
    else:
        print(f'{i} is not in the word.')
letter_in_word(guess_char, word_char)

# if guess_char[0] == word_char[0]:
#     print(f'Match!')