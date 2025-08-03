print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+F2/CTRL+break.
""")

# import time

# Write a for loop that counts to five.
# Body of the loop - print the loop iteration number and the word "Mississippi".
# Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

# for a in range(1,6):
#     print(a,"Mississippi")
#     time.sleep(1)
# print("Ready or not, here I come!")
#########################################################################################
# while True:
#     word = str(input("Say any word but chupacabra:"))
#     if word == "chupacabra":
#         print("You've successfully left the loop.")
#         break
#     print("Non, monsieur.")
#########################################################################################
# Scenario
#
# The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.
#
# It can be used with both the while and for loops.
#
# Your task here is very special: you must design a vowel eater! Write a program that uses:
#
#     a for loop;
#     the concept of conditional execution (if-elif-else)
#     the continue statement.
#
# Your program must:
#
#     ask the user to enter a word;
#     use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon – don't worry;
#     use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#     print the uneaten letters to the screen, each one of them on a separate line.
#
# Test your program with the data we've provided for you.
#########################################################################################
# user_word = str(input("Give cookie!"))
# user_word = user_word.upper()
#
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         print(str(letter))
#########################################################################################
# word_without_vowels = ""
# user_word = str(input("Give me cookie!"))
# user_word = user_word.upper()
#
# for letter in user_word:
#     if letter != "A":
#         if letter != "E":
#             if letter != "I":
#                 if letter != "O":
#                     if letter != "U":
#                         word_without_vowels += letter
#                         continue
# print(word_without_vowels)
#########################################################################################
# height = 0
# blocks = int(input("Enter the number of blocks: "))
#
# while True:
#     if blocks > height:
#         height += 1
#         blocks -= height
#     else:
#         break
#
# # final output
# print("The height of the pyramid:", height)
#########################################################################################
# c0 = int(input("Designate initial value:"))
# count_turns = 0
# while True:
#     if c0 != 1:
#         if c0 % 2 == 0:
#             c0 = c0 // 2
#         else:
#             c0 = int(3 * c0 + 1)
#         print(c0)
#         count_turns += 1
#     else:
#         break
# print("c0 value:",c0,",turns:",count_turns)
#########################################################################################
# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)
#########################################################################################
# x = 1
# while x < 11:
#     if x % 2 > 0:
#         print(x)
#     x += 1
# print("Done")
#########################################################################################
name = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        print(name)
        break
    else:
        name += ch
