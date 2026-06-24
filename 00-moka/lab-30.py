miles_in_meters = 1609.344 # miles in meters
gallon_in_liters = 3.785411784 # gallons in liters

def liters_100km_to_miles_gallon(liters):
  galons = liters / gallon_in_liters
  
  # *100 because we're converting to 100km
  miles_in_100km = (1000/miles_in_meters) * 100
  
  return miles_in_100km/galons

def miles_gallon_to_liters_100km(miles):
  one_hundred_kilometers = (miles * miles_in_meters) / 100_000
  
  return gallon_in_liters/one_hundred_kilometers

print("""
Expected output:
60.31143162393162
31.36194444444444
23.52145833333333
3.9007393587617467
7.490910297239916
10.009131205673757
""")

print("My output")
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

