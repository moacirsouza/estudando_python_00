hat_list = [1,2,3,4,5]
# this is an existing list of numbers
print("The original list is:", hat_list)

#step 1: write a line of code that prompts the user
user_number = int(input("Type a number: "))
#replace the middle number with an integer number enter by user
hat_list[2] = user_number
print("Replacing the middle number from hat_list:", hat_list)

#step 2: write a line of code that removes the last element from the list
del hat_list[4]
print("Deleting the last element from list: ", hat_list)

#step 3: write one line of code that prints the length of the existing list.
print("The new list is:", hat_list)
print("The list contains:", len(hat_list), "itens")