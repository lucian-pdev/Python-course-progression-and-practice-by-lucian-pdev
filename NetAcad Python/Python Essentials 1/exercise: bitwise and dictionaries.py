import random


# function
def spawn_random_mob():
    """Outputs the names (as strings) of a monster."""
    # lists to draw words from
    monster_type = {    0b01: "goblin",   0b10: "kobold",    0b11: "rat"}
    rarity = {          0b01: "common",   0b10: "rare",      0b11: "legendary"}
    strength = {        0b01: "",         0b10: "weakened",  0b11: "elite"}
    element = {         0b01: "",         0b10: "burning",   0b11: "wet"}
    dictionaries = [ strength, element, rarity, monster_type ]
    # initialising
    monster_name = ""
    # read byte_value and grab words from list
    for word in dictionaries:
        spawn_seed = random.randint(0b01, 0b11)
        print(f"[DEBUG] spawn seed (binary) : {spawn_seed:03b} for {word}")
        monster_name += word[spawn_seed]
        if word != monster_type:
            if word[spawn_seed] != "":
                monster_name += " "
    return monster_name


# main block
if __name__ == "__main__":
    # print(f"Mob name string = {mob_name_data[1]}, mob name as list = {mob_name_data[0]}")
    print(spawn_random_mob())
