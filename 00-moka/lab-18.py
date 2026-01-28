print("""
Welcome to rat race. You're stuck in
the loop unless you're able to guess
the secret word! Good luck!
""")

secret_word = "chupacabra"

while True:
  guessed_word = input("Guess the secret word: ")

  if guessed_word == secret_word:
    print("You've successfully left the loop.")
    break

  print("Sorry, that's not it. Try again...")

