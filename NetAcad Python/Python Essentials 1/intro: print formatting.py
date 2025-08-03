print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")
#########################################################################################
print("Hello World!")
print("Hello World!""\n""Works?")
# expected output: Programming***Essentials***in...Python
print("Programming","Essentials","in",sep="***",end="...")
print("Python")
#########################################################################################
#Try to:

#   minimize the number of print() function invocations by inserting the \n sequence into the strings;
#   make the arrow twice as large (but keep the proportions)
#   duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
#   remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error ‒ is this the place where the error really exists?
#   do the same with some of the parentheses;
#   change any of the print words into something else, differing only in case (e.g., Print) ‒ what happens now?
#   replace some of the quotes with apostrophes; watch what happens carefully.
#########################################################################################
# # Original
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
#########################################################################################
# one line
print("     *\n","   * *\n","  *   *\n"," *     *\n","***   ***\n","  *   *\n","  *   *\n","  *****")
#########################################################################################
# double size
print(" "*10,"*")                                                                                                         #11 elements
print(" "*9,"*","*")                                                                                                      #13
print(" "*8,"*"," "*1,"*")                                                                                                #14
print(" "*7,"*"," "*3,"*")                                                                                                #15
print(" "*6,"*"," "*5,"*")                                                                                                #16
print(" "*5,"*"," "*7,"*")                                                                                                #17
print(" "*4,"*"," "*9,"*")                                                                                                #18
print(" "*3,"*"," "*11,"*")                                                                                               #19
print(" "*2,"*"," "*13,"*")                                                                                               #20
print(" "*1,"*"," "*15,"*")                                                                                               #21
print(" "*0,"*"*6," "*7,"*"*6)                                                                                            #23
print(" "*5,"*"," "*7,"*")                                                                                                #
print(" "*5,"*"," "*7,"*")                                                                                                #
print(" "*5,"*"," "*7,"*")                                                                                                #
print(" "*5,"*"," "*7,"*")                                                                                                #
print(" "*5,"*"," "*7,"*")                                                                                                #
print(" "*5,"*"*11)                                                                                                       #
#########################################################################################
# 2 arrows
print(" "*4,"*"*1," "*9,"*"*1)                                                                                             #19 elements
print(" "*3,"*"*1,"*"*1," "*7,"*"*1,"*"*1)                                                                                 #20
print(" "*2,"*"*1," "*1,"*"*1," "*5,"*"*1," "*1,"*"*1)                                                                     #21
print(" "*1,"*"*1," "*3,"*"*1," "*3,"*"*1," "*3,"*"*1)                                                                     #22
print(" "*0,"*"*3," "*1,"*"*3," "*1,"*"*3," "*1,"*"*3)                                                                     #23
print(" "*2,"*"*1," "*1,"*"*1," "*5,"*"*1," "*1,"*"*1)                                                                     #21
print(" "*2,"*"*1," "*1,"*"*1," "*5,"*"*1," "*1,"*"*1)                                                                     #21
print(" "*2,"*"*1," "*1,"*"*1," "*5,"*"*1," "*1,"*"*1)                                                                     #21
print(" "*2,"*"*5," "*5,"*"*5)                                                                                             #21

#########################################################################################
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
#########################################################################################
