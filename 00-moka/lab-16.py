secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guessed_number = int(input("Try to guess the number: "))

while guessed_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guessed_number = int(input("Try to guess the number: "))

print("Well done, muggle! You are free now.")

