### Valores de referência
###
### +---------------+---------------------------------------+
### |     Input     |            Expected Output            |
### +---------------+---------------------------------------+
### | spathiphyllum |       No, I want a big Spathiphyllum! |
### +---------------+---------------------------------------+
### | pelargonium   |       Spathiphyllum! Not pelargonium! |
### +---------------+---------------------------------------+
### | Spathiphyllum | Spathiphyllum is the best plant ever! |
### +---------------+---------------------------------------+

plant_name = input("What's your favourite plant? ")

if plant_name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant_name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not " + plant_name + "!")
