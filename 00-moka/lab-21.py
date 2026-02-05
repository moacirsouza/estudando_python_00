blocks = int(input("Enter the number of blocks: "))

layer=0

for block in range(blocks):
    layer += (block+1)

    # print("Uma pirâmide de altura", block+1, "tem, no máximo,", layer, "bloco(s).")
    blocks_left = blocks - layer
    # print(blocks_left)
    
    if blocks_left < 0:
        height = block
        break

print("The height of the pyramid:", height)
