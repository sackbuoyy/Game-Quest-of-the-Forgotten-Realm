import random

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.health = 100
        self.inventory = []
        if player_class == "Warrior":
            self.attack = 15
            self.special_ability = "Power Strike"
            self.defense = 10
        elif player_class == "Mage":
            self.attack = 10
            self.special_ability = "Fireball"
            self.defense = 5
        elif player_class == "Rogue":
            self.attack = 12
            self.special_ability = "Stealth Attack"
            self.defense = 7

    def attack_enemy(self, enemy):
        damage = random.randint(5, self.attack)
        if random.choice([True, False]):
            damage += self.attack // 2
            print("Critical Hit!")
        enemy.health -= damage
        print(f"You strike {enemy.name} for {damage} damage!")

    def use_special_ability(self, enemy):
        if self.player_class == "Warrior":
            damage = random.randint(20, 30)
        elif self.player_class == "Mage":
            damage = random.randint(25, 35)
        elif self.player_class == "Rogue":
            damage = random.randint(15, 25) + random.randint(10, 20)
        enemy.health -= damage
        print(f"You unleash {self.special_ability} on {enemy.name} for {damage} damage!")

    def defend(self, enemy):
        damage = max(0, random.randint(5, enemy.attack) - self.defense)
        self.health -= damage
        print(f"You defend against {enemy.name}'s attack, reducing damage to {damage}!")

    def is_alive(self):
        return self.health > 0

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You found a {item}!")

    def heal(self):
        if "Potion" in self.inventory:
            self.health = min(100, self.health + 20)
            self.inventory.remove("Potion")
            print("You drink a Potion and restore 20 health!")
        elif "Elixir" in self.inventory:
            self.health = 100
            self.inventory.remove("Elixir")
            print("You drink an Elixir and fully restore your health!")
        else:
            print("You're out of healing items!")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_player(self, player):
        damage = random.randint(5, self.attack)
        player.health -= damage
        print(f"{self.name} hits you for {damage} damage!")

    def is_alive(self):
        return self.health > 0

class Boss(Enemy):
    def __init__(self):
        super().__init__("Dark Lord", 150, 25)
        self.special_attack_chance = 0.3

    def special_attack(self, player):
        if random.random() < self.special_attack_chance:
            damage = random.randint(20, 35)
            player.health -= damage
            print("The Dark Lord unleashes a devastating attack!")

class Game:
    def __init__(self):
        self.player = None
        self.locations = ["Enchanted Forest", "Shadowy Cave", "Abandoned Village", "Cursed Ruins"]
        self.enemies = [Enemy("Goblin", 30, 10), Enemy("Orc", 50, 15), Enemy("Undead Knight", 60, 20)]
        self.boss = Boss()
        self.game_over = False

    def start(self):
        print("The Quest of the Forgotten Realm begins!")
        self.choose_class()
        while not self.game_over:
            self.main_menu()

    def choose_class(self):
        print("Choose your path:")
        print("1. Warrior - Strength and Defense")
        print("2. Mage - Magic and Power")
        print("3. Rogue - Speed and Stealth")
        choice = input("Enter the number of your class: ")
        if choice == "1":
            self.player = Player("Hero", "Warrior")
        elif choice == "2":
            self.player = Player("Hero", "Mage")
        elif choice == "3":
            self.player = Player("Hero", "Rogue")
        else:
            print("Defaulting to Warrior.")
            self.player = Player("Hero", "Warrior")
        self.player.name = input("Enter your character's name: ")

    def main_menu(self):
        print("\nWhat will you do?")
        print("1. Explore")
        print("2. View Inventory")
        print("3. Heal")
        print("4. Use Special Ability")
        print("5. Quit")
        choice = input("Choose an action: ")
        if choice == "1":
            self.explore()
        elif choice == "2":
            self.view_inventory()
        elif choice == "3":
            self.player.heal()
        elif choice == "4":
            self.use_special_ability()
        elif choice == "5":
            self.quit_game()
        else:
            print("Invalid choice!")

    def explore(self):
        location = random.choice(self.locations)
        print(f"\nYou venture into the {location}.")
        if random.choice([True, False]):
            self.encounter_enemy()
        else:
            self.find_item()
        if not self.enemies and self.player.is_alive():
            print("A dark presence draws near...")
            self.final_boss_battle()

    def encounter_enemy(self):
        enemy = random.choice(self.enemies)
        print(f"A {enemy.name} emerges from the shadows!")
        while enemy.is_alive() and self.player.is_alive():
            print(f"\nYour Health: {self.player.health}")
            print(f"{enemy.name}'s Health: {enemy.health}")
            print("1. Attack")
            print("2. Defend")
            print("3. Run")
            choice = input("Choose an action: ")
            if choice == "1":
                self.player.attack_enemy(enemy)
                if enemy.is_alive():
                    enemy.attack_player(self.player)
            elif choice == "2":
                self.player.defend(enemy)
            elif choice == "3":
                print("You retreat!")
                break
            else:
                print("Invalid choice!")
        if not self.player.is_alive():
            self.game_over = True
            print("You have fallen. The realm is lost.")

    def find_item(self):
        item = random.choice(["Potion", "Elixir", "Magic Scroll", "Shield"])
        print(f"While exploring, you discover a {item}!")
        self.player.add_to_inventory(item)

    def use_special_ability(self):
        if not self.enemies:
            print("No enemies to use your special ability on!")
            return
        enemy = random.choice(self.enemies)
        self.player.use_special_ability(enemy)
        if not enemy.is_alive():
            print(f"The {enemy.name} has been vanquished!")
            self.player.add_to_inventory(random.choice(["Potion", "Elixir"]))
            self.enemies.remove(enemy)
        if not self.player.is_alive():
            self.game_over = True
            print("Your journey ends here...")

    def final_boss_battle(self):
        print("\nThe Dark Lord stands before you!")
        while self.boss.is_alive() and self.player.is_alive():
            print(f"\nYour Health: {self.player.health}")
            print(f"{self.boss.name}'s Health: {self.boss.health}")
            print("1. Attack")
            print("2. Defend")
            print("3. Use Special Ability")
            choice = input("Choose an action: ")
            if choice == "1":
                self.player.attack_enemy(self.boss)
                if self.boss.is_alive():
                    self.boss.special_attack(self.player)
            elif choice == "2":
                self.player.defend(self.boss)
            elif choice == "3":
                self.player.use_special_ability(self.boss)
            else:
                print("Invalid choice!")
        if not self.player.is_alive():
            self.game_over = True
            print("The Dark Lord has triumphed. Your quest ends in darkness.")
        else:
            print("Victory! You have defeated the Dark Lord and saved the realm!")

    def view_inventory(self):
        print("\nInventory:")
        for item in self.player.inventory:
            print(f"- {item}")
        print(f"Health: {self.player.health}")

    def quit_game(self):
        print("The realm awaits your return...")
        self.game_over = True

game = Game()
game.start()
