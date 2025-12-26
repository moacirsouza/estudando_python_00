### Valores de referência para x e y
###
### +----+------+
### | x  |  y   |
### +----+------+
### | 0  | -1.0 |
### +----+------+
### | 1  | 3.0  |
### +----+------+
### | -1 | -9.0 |
### +----+------+

# hardcode your test data here
x = 0

### Não é obrigatório forçar x a ser float, mas fica claro que, fazendo isto,
### todos os resultados retornam com este tipo
x = float(x)

### Neste caso, o uso dos parênteses não altera o resultado da operação, embora
### aumente a legibilidade do código. O teste pode ser realizado facilmente,
### alternando a linha em que 'y' recebe a respectiva atribuição por qualquer
### uma das linhas comentadas abaixo
#y=(3*x**3) - (2*x**2) + 3*x - 1
#y=3*x**3 - 2*x**2 + 3*x - 1
y=(3*(x**3)) - (2*(x**2)) + 3*x - 1

print("y =", y)
