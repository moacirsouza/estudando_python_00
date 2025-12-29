hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
### Agrupar o cálculo na variável intermediária 'duration_in_minutes',
### pode parecer excesso de cuidado, mas ajuda na hora de reescrever
### código. Por exemplo, se precisarmos alterar o nome da variáveis
### 'mins', só será necessário editar o código neste ponto
duration_in_minutes = mins + dura

### A divisão inteira por 60 nos dá a duração, em horas, do evento,
### enquanto o resto da divisão por 24, garante que o relógio "gira"
### quando atinge a meia-noite
final_hours = (hour + duration_in_minutes // 60) % 24

### O resto da divisão de 'duration_in_minutes' por 60, nos mostra
### em que ponto do tempo, em minutos, o evento acabou
final_minutes = duration_in_minutes % 60

### Foi usado o argumento de palavra-chave 'sep', para formatar a saída
### de acordo com o que foi solicitado
print(final_hours, final_minutes, sep=":")
