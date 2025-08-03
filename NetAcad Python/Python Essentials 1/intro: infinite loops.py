print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input())
while number != secret_number:
    print("""Ha ha! You're stuck in my loop! 
    So, what is the secret number?""")
    number = int(input())
print("Well done, muggle! You are free now.")
