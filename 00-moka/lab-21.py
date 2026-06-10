blocks = int(input("Enter the number of blocks: "))

height = 0
block='[]'
desenho = []

while True:
  height += 1
  next_layer = height + 1
  blocks -= next_layer
  desenho.append(block*height)

  if blocks <= 0:
    for i in range(height, 0, -1):
      print(f'{desenho[len(desenho)-i]: >{(i-1)+len(desenho[len(desenho)-i])}}')

    break

print("The height of the pyramid:", height)
