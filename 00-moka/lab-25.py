my_list = [0, 956, 3, 1, 4, 2, 4, 0, 4, 2, 6, 2, 9, 9]

### Creates a copy of the original list 
list_copy = my_list[:]

### Creates 'final_list' as an intermediaty, empty list to hold all the 
### non-duplicate values
final_list = []

### Runs through the entire list
for i in range(len(list_copy)):

  ### Checks if the first value in 'list_copy' does NOT yet belong to 
  ### 'final_list'. If that's the case, appends it to 'final_list'
  if list_copy[0] not in final_list:
    final_list.append(list_copy[0])

  ### This will ALWAYS execute, ultimately transforming 'list_copy' into an 
  ### empty list. BUT the previous 'if' guarantees that any value that still 
  ### doesn't belong to 'final_list' will be, first, copied to it
  del list_copy[0]

### Uncomment the next 'print' to validate that 'list_copy' will be empty at 
### the end of the execution
# print("This is what is left in 'list_copy':", list_copy)

### Copies 'final_list' over 'my_list' to show the final result
my_list=final_list[:]

print("The list with unique elements only:")
print(my_list)
