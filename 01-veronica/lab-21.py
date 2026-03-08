blocks = int(input("Enter the number of blocks: "))

height = 0
# height will be the #of blocks plus 1 blocks. 
#so for the next layer I will need to have the height + 1 block
#if the # of blocks is < or equal to the next layer it is not possible to have a new layer

while True:
  height += 1
  next_layer = height + 1
  blocks -= next_layer

# if the # of blocks is < or = zero is not possible to have a new layer so break the code
  if blocks <= 0:
    break

print("The height of the pyramid:", height)
