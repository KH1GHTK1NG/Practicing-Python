class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.mana = 50
        self.experience = 0
        self.inventory = []
        self.abilities = {}

    def gain_xp(self, amount):
        self.experience += amount

    def level_up(self):
        self.level += 1
        self.health = 100
        self.mana = 50

    def take_damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health += amount

    def learn_ability(self, ability, power):
        self.abilities[ability] = power

    def use_ability(self, ability):
        if ability in self.abilities:
            print(f"{self.name} uses {ability} with power {self.abilities[ability]}")
        else:
            print(f"{self.name} has not learned {ability} yet.")

    def attack(self, enemy):
        if isinstance(enemy, Enemy):
            enemy.health -= 10
            print(f"{self.name} attacks {enemy.name} for 10 damage!")
        else:
            print("Invalid target.")

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print(f"Experience: {self.experience}")
        print("Inventory: ", self.inventory)
        print("Abilities: ", self.abilities)

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

player = Character("Knight")
player.show_stats()