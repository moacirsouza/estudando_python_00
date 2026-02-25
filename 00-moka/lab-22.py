while True:
  c0 = int(input("Enter c0 value: "))
  
  if c0 <= 0:
    print("ATTENTION: c0 has to be a positive integer")
    continue

  steps = 0

  while c0 != 1:
    if c0 % 2 == 0:
      c0 = c0 // 2
    else:
      c0 = 3 * c0 + 1
    
    steps += 1
    print(c0)
  
  break

print("steps =", steps)
