import random

# Player class to handle player attributes
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.inventory = []

    def attack_enemy(self, enemy):
        damage = random.randint(5, 15)
        enemy.health -= damage
        print(f"You attack {enemy.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} added to your inventory.")

    def heal(self):
        if "Potion" in self.inventory:
            self.health = min(100, self.health + 20)
            self.inventory.remove("Potion")
            print("You used a Potion and restored 20 health!")
        else:
            print("No Potions left!")

# Enemy class to handle enemy attributes
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_player(self, player):
        damage = random.randint(5, self.attack)
        player.health -= damage
        print(f"{self.name} attacks you for {damage} damage!")

    def is_alive(self):
        return self.health > 0

# Game class to handle the game flow
class Game:
    def __init__(self):
        self.player = Player("Hero")
        self.locations = ["Forest", "Cave", "Village"]
        self.enemies = [Enemy("Goblin", 30, 10), Enemy("Orc", 50, 15), Enemy("Dragon", 100, 20)]
        self.game_over = False

    def start(self):
        print("Welcome to the Adventure Game!")
        self.player.name = input("Enter your character's name: ")
        while not self.game_over:
            self.main_menu()

    def main_menu(self):
        print("\nMain Menu:")
        print("1. Explore")
        print("2. View Inventory")
        print("3. Heal")
        print("4. Quit")
        choice = input("Choose an action: ")
        if choice == "1":
            self.explore()
        elif choice == "2":
            self.view_inventory()
        elif choice == "3":
            self.player.heal()
        elif choice == "4":
            self.quit_game()
        else:
            print("Invalid choice!")

    def explore(self):
        location = random.choice(self.locations)
        print(f"\nYou explore the {location}.")
        if random.choice([True, False]):
            self.encounter_enemy()
        else:
            self.find_item()

    def encounter_enemy(self):
        enemy = random.choice(self.enemies)
        print(f"A wild {enemy.name} appears!")
        while enemy.is_alive() and self.player.is_alive():
            print(f"\nYour Health: {self.player.health}")
            print(f"{enemy.name}'s Health: {enemy.health}")
            print("1. Attack")
            print("2. Run")
            choice = input("Choose an action: ")
            if choice == "1":
                self.player.attack_enemy(enemy)
                if enemy.is_alive():
                    enemy.attack_player(self.player)
                else:
                    print(f"You defeated the {enemy.name}!")
                    self.player.add_to_inventory("Potion")
            elif choice == "2":
                print("You ran away!")
                break
            else:
                print("Invalid choice!")
        if not self.player.is_alive():
            self.game_over = True
            print("You died. Game Over.")

    def find_item(self):
        item = random.choice(["Potion", "Sword", "Shield"])
        print(f"You found a {item}!")
        self.player.add_to_inventory(item)

    def view_inventory(self):
        print("\nInventory:")
        for item in self.player.inventory:
            print(f"- {item}")
        print(f"Health: {self.player.health}")

    def quit_game(self):
        print("Thank you for playing!")
        self.game_over = True

# Start the game
game = Game()
game.start()
