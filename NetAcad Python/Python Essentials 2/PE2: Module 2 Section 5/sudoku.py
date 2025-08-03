# sudoku
# check if all elements on the board are digits
# check if each row contains all digits
# check if each column contains all digits
# check if each 3x3 square contains all digits

board_9x9 = []

# check if all elements on the board are digits and make the list comprehension
user_input = input("Enter the 9x9 sudoku board: ").replace(' ', '')
if user_input.isdigit():
    if len(user_input) != 81:
        print("Invalid input. Please enter a 9x9 sudoku board.")
        exit(0)
    list_input = []
    index = 0
    for i in user_input:
        list_input.append(i)
    for col in range(9):
        for row in range(9):
            board_9x9.append(list_input[index])
            index += 1
else:
    print("Invalid input. Please enter a 9x9 sudoku board.")
    exit(0)

# test print of the board
print(f"Board before checks:\n")
ind = 0; 
for i in range(9): 
    print(' '.join(board_9x9[ind:ind+9]))
    ind += 9
print("\n")


# universal check, if it turns false, all loops stop and the board is a failure
correct = True

# fun to build check dictionary
def make_check_dict():
    check_dict = {}
    for i in range(1, 10):
        check_dict[str(i)] = False
    return check_dict
ref_dict = make_check_dict()

# check if all rows contain all digits
while correct:
    check_dict = ref_dict
    for i in range(9):
        for j in range(9):
            if board_9x9[i * 9 + j] in check_dict:
                check_dict[board_9x9[i * 9 + j]] = True
                # print(f"{board_9x9[i*9+j]} in row {i+1} column {j+1}")
        if False in check_dict.values():
            correct = False
            print("The rows do not contain all the digits.")
            break
        check_dict = ref_dict
    print("The rows contain all the digits.")
    break

# check if all columns contain all digits
while correct:
    check_dict = ref_dict
    for i in range(9):
        for j in range(9):
            if board_9x9[j*9+i] in check_dict:
                check_dict[board_9x9[j * 9 + i]] = True
                # print(f"{board_9x9[j*9+i]} in row {j+1} column {i+1}")
        if False in check_dict.values():
            correct = False
            print("The columns do not contain all the digits.")
            break
        check_dict = ref_dict
    print("The columns contain all the digits.")
    break

# check if each 3x3 sub-square contains all digits
while correct:
    check_dict = ref_dict
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    index = (i*3+k)*9+j*3+l
                    if board_9x9[index] in check_dict:
                        check_dict[board_9x9[index]] = True
                        # print(f"{board_9x9[index]} in row {k+1} column {l+1}")
            if False in check_dict.values():
                correct = False
                print("The 3x3 sub-squares do not contain all the digits.")
                break
            check_dict = ref_dict
    print("The 3x3 sub-squares contain all the digits.")
    break

# End banner
if correct:
    print("This sudoku board is complete.")