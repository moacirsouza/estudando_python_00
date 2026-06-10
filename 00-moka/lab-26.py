def is_year_leap(ano):
### Código inspirado em uma versão da validação de ano bissexto, do projeto
### NADAS, hospedado em: https://bit.ly/4vG3ry5
### 
### NOTA: Este código é 'confuso' de entender, porque ele utiliza as noções de 
### Lógica Reversa (verdadeiro se NÃO for assim, falso se FOR assim etc.). É
### importante revisá-lo com cautela, anotando todas as possibilidades em uma
### lista, para compreender bem o funcionamento
  if ano%4 != 0 or (ano%400 != 0 and ano%100 == 0):
    retorno = False
    # print('{} é um ano comum.'.format(ano))
  else:
    retorno = True
  # print('{} é um ano Bissexto'.format(ano))

### Remova os comentários da primeira linha do bloco a seguir, para uma versão 
### mais direta das regras de validação do ano bissexto
#  if ano%4 != 0:
#    retorno = False
#    # print(comum)
#  elif ano%100 != 0:
#    retorno = True
#    # print(bissexto)
#  elif ano%400 != 0:
#    retorno = False
#    # print(comum)
#  else:
#    retorno = True

  return retorno


test_data =    [ 1900, 2000, 2016,  1987,  1982, 3004]
test_results = [False, True, True, False, False, True]

for i in range(len(test_data)):
  yr = test_data[i]
  print(yr,"->",end=" ")
  result = is_year_leap(yr)
  if result == test_results[i]:
    print("OK")
  else:
    print("Failed")
