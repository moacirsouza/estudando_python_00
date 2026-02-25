word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
# Complete the body of the loop.
 
user_word = input("Enter a word: ").upper()

for letter in user_word:
   
    if letter in "A,E,I,O,U":
        continue

    word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)