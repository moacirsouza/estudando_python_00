### Valores de referência para x
### x = 0, y = -1.0
### x = 1, y = 3.0
### x = -1, y = -9.0
x = 0 # hardcode your test data here

### Não é obrigatório forçar x a ser float,
### mas fica claro que fazendo isto, todos
### os resultados retornam com este tipo
x = float(x)

y=(3*(x**3)) - (2*(x**2)) + 3*x - 1
### O uso dos parênteses, neste caso, não altera
### o resultado da operação, embora aumente a
### legibilidade do código
#y=(3*x**3) - (2*x**2) + 3*x - 1
#y=3*x**3 - 2*x**2 + 3*x - 1

print("y =", y)
