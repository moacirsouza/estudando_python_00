while True:
  c0 = int(input("Enter with a number to c0: "))
  # check if the number is correct. 
  #If the condition is True (or if the number is > 0 so continue the loop)
  
  if c0 <= 0:
    print("The number should be higher than zero. Try again!!!")
    continue

  steps = 0

# while the number is different from 1, c0 is even number (or % 2 = 0) 
# the c0 will be the inter division.
# else the c0 will be 3 multiplied by c0 + 1

  while c0 != 1:
    if c0 % 2 == 0:
      c0 = c0 // 2
    else:
      c0 = 3 * c0 + 1
    
    steps += 1
    print(c0)
  
  break

print("steps =", steps)