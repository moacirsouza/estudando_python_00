secret_word = "chupacabra"

while True:
    new_word = input("Type a word: ")

    if new_word == secret_word:
        print("You have successfully")
        break
    print("Sorry it is not the secret word, try again!")
