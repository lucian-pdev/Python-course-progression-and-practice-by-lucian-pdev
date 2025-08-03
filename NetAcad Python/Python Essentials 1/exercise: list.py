print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")
#####################################################################################
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:      # while sees True and uses the loop body
    swapped = False  # no swaps so far
    for h in range(len(my_list) - 1):   # h is the INDEX, not the value itself
        if my_list[h] > my_list[h + 1]:
            swapped = True  # a swap occurred!
            my_list[h], my_list[h + 1] = my_list[h + 1], my_list[h]

print(my_list)
#####################################################################################
list_to_sort = [8, 10, 6, 2, 4]
list_to_sort.sort()
print(list_to_sort)
#####################################################################################
duplicate_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
no_duplicate_list = []

for o in duplicate_list:
    if o not in no_duplicate_list:
        no_duplicate_list.append(o)

no_duplicate_list.sort()
print("The list with unique elements only:")
print(no_duplicate_list)
#####################################################################################
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # outputs True
print("A" not in my_list)  # outputs True
print(3 not in my_list)  # outputs True
print(False in my_list)  # outputs False

