year = int(input("Enter a year: "))

if year < 1582:
    response = "Not withing the Gregorian calendar period"
elif year %4 !=0:
    response =  "It is a common year"
elif year %100 !=0:
    response = "It is a leap year"
elif year %400 !=0:
    response = "It is a common year"
else:
    response = "It is a leap year!"

print(response)
