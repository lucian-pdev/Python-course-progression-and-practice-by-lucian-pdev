#!/usr/bin/env python3
    
def caesar_cypher( original, direction="code", shift=1):
    if direction.lower() == "decode":
        shift = shift * -1
    result = ""
    for char in original:
        if char.isalpha():
            if char.isupper():
                temp = (ord(char) - ord('A') + shift) % 26 + ord('A')
            else:
                temp = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result += chr(temp)
        else:
            result += char
    print(result)


if __name__=="__main__":
    direction = str(input("What shall I do? [CODE/decode]\n"))
    original = str(input("What do you wish you change?\n"))
    try:
        shift = int(input("What shift? [>0]\n"))
    except:
        print("That's not an integer, assuming default: 1")
        shift = 1
    caesar_cypher(original, direction, shift)
    exit
