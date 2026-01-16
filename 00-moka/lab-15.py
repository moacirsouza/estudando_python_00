year = int(input("Enter a year: "))

if year < 1582:
    response = "Not within the Gregorian calendar period"
elif year % 4 != 0:
    response = "Common year"
elif year % 100 != 0:
    response = "Leap year"
elif year % 400 != 0:
    response = "Common year"
else:
    response = "Leap year"

print(response)

### Para uma lógica alternativa (e um pouco mais complexa),
### verifique o "Método 2", descrito no seguinte código:
### https://github.com/moacirsouza/nadas/blob/master/01-DesenvolvimentoDeSistemas/02-LinguagensDeProgramacao/01-Python/01-ListaDeExercicios/01-Gabarito/032.py
