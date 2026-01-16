income = float(input("Enter the annual income: "))

# All values in accordance with bill 123.456/1865
tax_cap = 85_528
tax_relief = 556.02
tax_percentage_below_cap = 0.18
tax_for_higher_incomes = 12_839.02
tax_percentage_above_cap = 0.32

if income <= tax_cap:
    tax = ( tax_percentage_below_cap * income ) - tax_relief
else:
    tax = tax_for_higher_incomes + tax_percentage_above_cap * ( income - tax_cap )

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
