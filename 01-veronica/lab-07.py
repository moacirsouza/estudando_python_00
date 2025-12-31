#Consider that sample input is x = 0, or x = 1, or x = -1.
#The expected output will be: y = -1,0, or y = 3.0, or y = - 9.0, respectivelly.

x =  1.0
x = float(x)
y=(3*(x**3)) - (2*(x**2)) + 3*x - 1
print("y =", y)

# Pay attention to the parentheses, another way to write this expression with reduced number of parentheses is:
y = (3*x**3) - (2*x**2) + 3*x - 1
print("y =", y)