#  Exercise 1: “Creature Feature” — Basic Class Design

# Task: Create a Python class named Creature with the following specifications:

#     Has attributes: name (str), species (str), and hit_points (int)

#     A method take_damage(amount) that subtracts amount from hit_points

#     A method is_alive() that returns True if hit_points is greater than 0

#     Add a class-level variable that tracks how many creatures have been created


class Creature:
    creatures_count = 0
    
    def __init__(self, name, species, hit_points):
        Creature.creatures_count += 1
        self.name = name
        self.species = species
        self.hit_points = hit_points

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            print(f"{self.name} has died.")

    def is_alive(self):
        return self.hit_points > 0

    def __str__(self):
        return f'{self.name}, the {self.species}, has {self.hit_points} hit points.'
    
Rattle_snake = Creature('Rattle_snake', 'snake', 20)
print(f'There {"is" if Creature.creatures_count == 1 else "are"} {Creature.creatures_count} creatures currently.')
print(Rattle_snake)
Rattle_snake.take_damage(5)
print(f"Rattle_snake has been hit for 5 damage!")
Rattle_snake.is_alive()
print(Rattle_snake)
Rattle_snake.take_damage(5)
print(f"Rattle_snake has been hit for 5 damage!")
print(Rattle_snake.is_alive())


# Exercise 2: “Potion Mixology” — Inheritance and Method Overriding

# Task: You have a base Potion class with name and potency. Create two subclasses:

#     HealingPotion: restores health

#     PoisonPotion: reduces health

# Each should have a use(target) method that affects the target creature differently.

# Add a __str__() method to each potion class for readable output

class Potion:
    def __init__(self, name, potency):
        self.name = name
        self.potency = potency if potency > 0 else abs(potency)

    def use(self, target):
        target.hit_points += self.potency
        print(f"Using {self.name} on {target.name}, effect: {self.potency} hit points.")
        
    def __str__(self):
        return f"{self.name} (potency: {self.potency})"

class HealingPotion(Potion):
    def use(self, target):
        super().use(target)
        
    def __str__(self):
        return f"Healing potion: {self.name} (potency: {abs(self.potency)})"

class PoisonPotion(Potion):
    def use(self, target):
        target.take_damage(self.potency)
        
    def __str__(self):
        return f'Poison potion: {self.name} (potency: {abs(self.potency)})'


healing_potion = HealingPotion("Healing Potion", 10)
healing_potion.use(Rattle_snake)
print(Rattle_snake)
poison_potion = PoisonPotion("Poison Potion", -5)
poison_potion.use(Rattle_snake)
print(Rattle_snake)

# Exercise 3: “The Guild” — Composition and Interaction

# Task: Create a Guild class that manages multiple Creature members.

#     Add/remove creatures

#     Display all living members

#     Let guild members take turns fighting another guild
    
#     Track win/loss records for guild battles

#     Use type hints for method signatures

class Guild:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.wins = 0
        self.losses = 0

    def add_member(self, creature):
        self.members.append(creature)

    def remove_member(self, creature):
        self.members.remove(creature)

    def show_living(self):
        return f'In the guild {self.name}, the following members are alive: {", ".join([creature.name for creature in self.members if creature.is_alive()])}'

    def battle(self, other_guild):
        print(f"""Commencing guild war!\nThe guild {self.name} will attack the guild {other_guild.name}.\n""")
        temp_members = self.members[:]
        temp_enemies = other_guild.members[:]
        for member in temp_members:
            for enemy in temp_enemies:
                a = member.hit_points
                b = enemy.hit_points
                enemy.take_damage(abs(a))
                member.take_damage(abs(b))
                if not enemy.is_alive():
                    self.wins += 1
                    other_guild.losses += 1
                    print(f"{member.name} has defeated {enemy.name}.")
                    other_guild.remove_member(enemy)
                elif not member.is_alive():
                    self.losses += 1
                    other_guild.wins += 1
                    print(f"{enemy.name} has defeated {member.name}.")
                    self.remove_member(member)
        print(f"The guild war is over!\n{self.show_living()}\n{other_guild.show_living()}")
        if len(self.members) > len(other_guild.members):
            print(f"The guild {self.name} has won the battle.")
        elif len(self.members) < len(other_guild.members):
            print(f"The guild {other_guild.name} has won the battle.")
        else:
            print("The battle was a draw.")
        
        for creature in self.members:
            print(creature)
            
        for creature in other_guild.members:
            print(creature)
        
    def __str__(self):
        return f"The guild {self.name} has {len(self.members)} members. They have won {self.wins} times and lost {self.losses} members."


guild_Snakes = Guild("Guild Snakes")
guild_Rodents = Guild("Guild Rodents")

guild_Snakes.add_member(Rattle_snake)

for x in range(4):
    name = "Rat" + str(x)
    globals()[name] = Creature(name, "rodent", 1)
    guild_Rodents.add_member(globals()[name])

print(guild_Snakes)
print(guild_Rodents)


guild_Snakes.battle(guild_Rodents)

print(guild_Snakes)
print(guild_Rodents)

