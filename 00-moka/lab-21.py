blocks = int(input("Enter the number of blocks: "))

height = 0

while True:
  height += 1
  next_layer = height + 1
  blocks -= next_layer

  if blocks <= 0:
    break

print("The height of the pyramid:", height)
