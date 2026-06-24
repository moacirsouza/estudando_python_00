def is_prime(num):
  result = True

  for divisor in range(2, num):
    if num%divisor == 0:
      result = False
      break
  
  return result

for i in range(1, 1000):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

