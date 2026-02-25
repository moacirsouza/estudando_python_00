# Prompt the user to enter a word
# and assign it to the user_word variable.
# Complete the body of the for loop.

user_word = input("Type a word: ").upper()
for letter in user_word:
    if letter in "A,E,I,O,U":
        continue
    print(letter)