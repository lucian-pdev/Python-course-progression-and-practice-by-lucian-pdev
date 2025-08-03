# IBAN Checker
# This program checks if an IBAN is valid based on its length and country code.
iban_lengths = {
    "AL": 28, "AD": 24, "AT": 20, "AZ": 28, "BE": 16, "BA": 20,
    "BG": 22, "HR": 21, "CY": 28, "CZ": 24, "DK": 18, "EE": 20,
    "FI": 18, "FR": 27, "GE": 22, "DE": 22, "GI": 23, "GR": 27,
    "HU": 28, "IS": 26, "IE": 22, "IL": 23, "IT": 27, "LV": 21,
    "LI": 21, "LT": 20, "LU": 20, "MT": 31, "MD": 24, "MC": 27,
    "ME": 22, "NL": 18, "MK": 19, "NO": 15, "PL": 28, "PT": 25,
    "RO": 24, "SM": 27, "RS": 22, "SK": 24, "SI": 19, "ES": 24,
    "SE": 24, "CH": 21, "TR": 26, "UA": 29, "GB": 22, "VA": 22,
    "XK": 20
}


def is_valid_iban(iban):
    """Check if the IBAN is valid based on its length and country code."""
    # check country code and valid length
    country_code = iban[:2]
    if len(iban) != iban_lengths.get(country_code):
        return None
    # move initial characters
    iban = iban[4:] + iban[0:4]
    # replace each letter with 2 digis, where (A = 10, B = 11 ... Z = 35)
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    # calculate if the check-sum is valid
    if iban % 97 == 1:
        print("This is a valid IBAN.")
    else:
        print("This IBAN is invalid.")


if __name__ == "__main__":
    test_iban = input("Enter an IBAN: ").upper()
    test_iban = test_iban.replace(" ", "")
    if not test_iban.isalnum():
        print("Invalid characters found.")
    is_valid_iban(test_iban)




# # IBAN Validator.

# iban = input("Enter IBAN, please: ")
# iban = iban.replace(' ','')

# if not iban.isalnum():
#     print("You have entered invalid characters.")
# elif len(iban) < 15:
#     print("IBAN entered is too short.")
# elif len(iban) > 31:
#     print("IBAN entered is too long.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("IBAN entered is valid.")
#     else:
#         print("IBAN entered is invalid.")
    