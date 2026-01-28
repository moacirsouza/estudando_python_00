# Prompt the user to enter a word
# and assign it to the user_word variable.

# Receives and capitalises the user input, all at once
user_word = input("Enter a word: ").upper()

for letter in user_word:
  # Complete the body of the for loop.
  if letter in "AEIOU":
    continue

  print(letter)

