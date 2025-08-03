# Tuples
var = 123

t1 = (1,)
t2 = (2,)
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

# Print the values here.
print(f"look up boss's number results in {phone_numbers['boss']}")
print(dictionary["dog"])
print(dictionary["cat"])

# exercise 1: tuples and dictionary together
school_class = {}

while True:
    Name = str(input("Write name to proceed or enter to escape."))
    if Name == "":
        break
    Score = (input("Write score."))
    if Score == "":
        Score = (input("That is an invalid score, again."))
        if Score == "":
            break
        else:
            Score = float(Score)
    else:
        Score = float(Score)
    school_class[Name] = Score

print(school_class)

# given example for ex 1
school_class = {}

while True:
    name = input("Enter the student's name to proceed or enter to escape.")
    if name == '':
        break

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# exercise 2: using count()
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = 0
temp_list = []

for elem in tup:
    if elem not in temp_list:
        if tup.count(elem) > 1:
            print(tup.count(elem))
            duplicates += tup.count(elem)
            temp_list.append(elem)

print(f"We have {duplicates} duplicates.")  # outputs: 4

# exercise 3: combining dictionaries
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

# exercise 4: convert to tuple
my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)
print(t)

# Exercise 4: converting a tuple to a dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = {}
for key,value in colors:
    colors_dictionary[key] = value

print(colors_dictionary)

