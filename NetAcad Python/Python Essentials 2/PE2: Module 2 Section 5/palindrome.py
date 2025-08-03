# """A plaindrome is a text that has the exact form when it's read backwards."""

original = str(input("Give me a word:\n"))
original = original.upper()
original = original.replace(" ","")
temp = []
for chr in original:
    temp.append(chr)
# print(f"temp type = {type(temp)}, temp after split = \n {temp}")
temp.reverse()
# print(f"temp type = {type(temp)}, temp after reverse = \n {temp}")
reverse = ''.join(temp)
# print(f"temp type = {type(reverse)}, temp after join = \n {reverse}")
if original == "":
    palindrome = False
if original == reverse:
    palindrome = True
else:
    palindrome = False
if palindrome:
    print("That's a palindrome.")
else:
    print("That is not a palindrome.")