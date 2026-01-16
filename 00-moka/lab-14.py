income = float(input("Enter the annual income: "))

tax_cap = 85_528
tax_for_higher_incomes = 14_839.02

if income <= tax_cap:
    tax = ( 0.18 * income ) - 556.02
else:
    tax = tax_for_higher_incomes + 0.32 * ( income - tax_cap )

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
