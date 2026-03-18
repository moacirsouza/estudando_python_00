hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
user_input = int(input('Give me a number: '))
hat_list[2] = user_input

# Step 2: write a line of code that removes the last element from the list.
"""
Método mais direto, porem inflexível.
Se o tamanho da lista mudar, o resultado
vai ser diferente do esperado.
"""
#del hat_list[4]

"""
Método mais 'pytônico': Significa que a
a comunidade Python espera que a atividade
seja realizada desta forma.
"""
del hat_list[-1] 

"""
Método 'clássico' para descobrir o último
item da lista. Usado desde a década de 70,
quando a linguagem C foi criada.
"""
#del hat_list[ (len(hat_list) - 1) ]

# Not requested, but I'll leave the printing of the array anyway :)
print(hat_list)

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
