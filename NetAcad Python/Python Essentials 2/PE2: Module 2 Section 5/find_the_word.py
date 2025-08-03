# We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

# Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

# For example:

#     if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
#     if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as the letters "d", "o", or "g" don't appear in this order)

dict = {}
input_word = input("Enter a word: ").upper()
input_string = input("Enter a string: ").upper()

for l in input_word:
    dict[l] = False

for s in input_string:
    if s in dict:
        if dict[s] == False:
            dict[s] = True
        else:
            continue
    else:
        continue

if False in dict.values():
    print("No")
else:
    print("Yes")