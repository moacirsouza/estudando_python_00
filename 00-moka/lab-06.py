print("Conversion tests: Kilometers and Miles\n")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

print("\n===================================\n")

print("Conversion tests: Dollars and Reais\n")

dollars = 8.96
reais = 36.54
conversion_rate_dollar_to_real = 5.50

dollars_to_reais = dollars * conversion_rate_dollar_to_real
reais_to_dollars = reais / conversion_rate_dollar_to_real

print(dollars, "dollars is", round(dollars_to_reais, 2), "reais")
print(reais, "reais is", round(reais_to_dollars, 2), "dollars")
