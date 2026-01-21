income = float(input("Enter the annual income: "))
# to make the code better we can set variable for each value

citizen_income = 85_528
low_tax_percentage = 0.18
minus_income = 556.2
higher_income = 14_839.2
additional_percentage = 0.32
tax_over = 85_528

if income <= citizen_income:
    tax = (income * low_tax_percentage) - minus_income
else:
    tax = higher_income + additional_percentage * (income - citizen_income)

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")