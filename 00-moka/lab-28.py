def is_year_leap(ano):
  if ano%4 != 0 or (ano%400 != 0 and ano%100 == 0):
    retorno = False
  else:
    retorno = True
  
  return retorno


def days_in_month(year, month):
  mes = month-1
  ### Total de dias dos meses do ano, considerando a posição do mês
  ###       0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11
  meses =           [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  nomes_dos_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

  if is_year_leap(year):
    meses[1] = 29
  
  return [meses[mes], nomes_dos_meses[mes]]


test_years =   [1900, 2000, 2016, 1987]
test_months =  [   2,    2,    1,   11]
test_results = [  28,   29,   31,   30]

for i in range(len(test_years)):
  yr = test_years[i]
  mo = test_months[i]
  print(yr, mo, "->", end=" ")
  result = days_in_month(yr, mo)[0]
  if result == test_results[i]:
    print("OK")
  else:
    print("Failed")


def day_of_year(year, month, day):
  total_days = 0

  if is_year_leap(year):
    print('É bissexto')

  for i in range(month-1):
    total_days += days_in_month(year, i+1)[0]

  print("O dia ", day, " de ", days_in_month(year, month)[1], " é o ", total_days + day, "º dia do ano ", year, sep="")

print(day_of_year(2000, 8, 20))
