print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")
#####################################################################################
# I managed to make a tuple based conditional loop before the chapters with lists

# vowel = ("A", "E", "I", "O", "U")
# user_word = str(input("Give cookie!"))
# user_word = user_word.upper()
# for letter in user_word:
#     if letter not in vowel:
#         print(str(letter))
#     else:
#         continue
#####################################################################################
# Lists
# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
#
# # Step 1: write a line of code that prompts the user
# # to replace the middle number with an integer number entered by the user.
# hat_list[int(len(hat_list)/2)+(len(hat_list)%2>0)]=int(input("Give cookie count:"))
#
# # Step 2: write a line of code that removes the last element from the list.
# del hat_list[-1]
# # Step 3: write a line of code that prints the length of the existing list.
# print(f"The length of the list is:{len(hat_list)}.")
#
# print(hat_list)
#####################################################################################
beatles = []

# step 1
print("Step 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# step 2
print("Step 2:", beatles)
for i in range(0,2):
    beatles.append(input("New member?:"))

# step 3
print("Step 3:", beatles)
del beatles[-1]
del beatles[-1]

# step 4
print("Step 4:", beatles)
beatles.insert(0,"Ringo Starr")

# step 5
print("Step 5:", beatles)

# testing list length
print("The Fab", len(beatles))
