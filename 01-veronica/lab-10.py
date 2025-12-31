x = float(input("Enter value for x: "))
#Note: sample input 1, 10 and 100 will have an expected output of 0.60, 0.099, 0.0099, respectively

y = 1/(x+(1/(x+1/(x+1/x))))

# also we can reduce the number of parantheses using:
y = 1/(x+1/(x+1/(x+1/x)))

print("y =", y)