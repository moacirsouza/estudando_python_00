def is_year_leap(ano):
  if ano%4 != 0 or (ano%400 != 0 and ano%100 == 0):
    retorno = False
  else:
    retorno = True
  
  return retorno


def days_in_month(year, month):
  mes = month-1

  ### Total de dias dos meses do ano, considerando a posição do mês
  ###                 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11
  meses =           [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  nomes_dos_meses = [ 'Janeiro', 'Fevereiro',    'Março',    'Abril', 
                         'Maio',     'Junho',    'Julho',   'Agosto', 
                     'Setembro',   'Outubro', 'Novembro', 'Dezembro']

  if is_year_leap(year):
    meses[1] = 29
  
  return [meses[mes], nomes_dos_meses[mes]]


test_years =   [1900, 2000, 2016, 1987]
test_months =  [   2,    2,    1,   11]
test_results = [  28,   29,   31,   30]

#for i in range(len(test_years)):
#  yr = test_years[i]
#  mo = test_months[i]
#  print(yr, mo, "->", end=" ")
#  result = days_in_month(yr, mo)[0]
#  if result == test_results[i]:
#    print("OK")
#  else:
#    print("Failed")

def day_of_year(year, month, day):
  total_days = 0
  retorno = ""
  posicao_do_problema = "Erro. Valor de variável incorreto!\n"
  
  if year <= 0 or month <= 0 or day <= 0:
    posicao_do_problema += "O valor de 'ano', 'mês' ou 'dia' precisa ser um inteiro positivo, maior que zero!"
    retorno = None

  if month > 12:
    posicao_do_problema += "O valor máximo de 'mês' é 12!"
    retorno = None

  if day > 31:
    posicao_do_problema += "O valor máximo de 'dia' é 31!"
    retorno = None
  
  if retorno == None:
    return [retorno, posicao_do_problema]

  for i in range(month-1):
    total_days += days_in_month(year, i+1)[0]

  retorno = total_days + day

  return [retorno, [year, month, day, days_in_month(year, month)[1]]]


dias_passados = day_of_year(1904, 8, 22)

if dias_passados[0] == None:
  print(dias_passados[1])
else:
  print("O dia ", dias_passados[1][2], " de ", dias_passados[1][1], " (", dias_passados[1][3], ") é o ", dias_passados[0], "º dia do ano ", dias_passados[1][0], "!", sep="")
