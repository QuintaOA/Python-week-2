# Create an empty list
my_list = []

# Append values 10,20,30,40 to the empty created list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Appended value list: ",my_list)

# Insert the value 15 at the second position in the list.
my_list.insert(2,15)
print("Inserted value list: ",my_list)

# Extend my_list with another list :[50, 60, 70].
additional_list = [50,60,70]
my_list.extend(additional_list)
print("Additional List to inserted list: ", my_list)

# Remove the last element from my_list
del my_list[-1]
print("Last element deleted list: ", my_list)

# Sort my_list in ascending order
my_list.sort()
print("Sorted list in ascending order :",my_list)

# Find and print the index of the value 30 in my_list.
print(my_list[3])