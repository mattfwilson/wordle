word = 'light'
user_input = ''
result = None

guess = input("What is your first guess? ")

word_check = []
guess_check = []

# for letter in word:
#     pos = word.find(letter)
#     word_check.append(pos)
# print(word_check)

for letter in guess:
    if letter in word:
        pos = word.find(letter)
        guess_check.append(pos)

print(guess_check)

for match in guess_check:
    if match == word.find(str(match)):
        word.replace(match, "*")

print(word)


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
    