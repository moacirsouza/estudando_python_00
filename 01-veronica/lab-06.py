kilometers = 12.25
miles = 7.38

miles_to_kilometers = (miles * 1.61)
kilometers_to_miles = (kilometers / 1.61)

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

print("========================================================\n")
print("New test: Converting dollar and reais!\n")

dollars = 10.0
reais = 5.0
conversion_dollar_to_real = 5.53

print("Veronica has:", reais, "reais.", "This correspond to:", round(reais/conversion_dollar_to_real,3), "dollars.")
print("Veronica came back from US with:", dollars, "dollars.", "This value correspond to:", round(dollars*conversion_dollar_to_real, 2), "reais.")

#Another easier way to do this is to use variables to convert dollars to reais or reais to dollars.

dollar_to_reais = dollars * conversion_dollar_to_real
reais_to_dollar = reais/conversion_dollar_to_real

print(dollars, "dollars is", round(dollars*conversion_dollar_to_real, 2), "reais!")
print(reais, "reais is", round(reais/conversion_dollar_to_real, 3), "dollars!")

