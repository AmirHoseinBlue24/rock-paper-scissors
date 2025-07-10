import random

class Game:
    def __init__(self):
        self.user_choice = 0
        self.computer_choice = 0
        self.items = {1: "rock", 2: "paper", 3: "scissors"}
        self.winners = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    def get_user_choice(self):
        print("\n1. Rock\n2. Paper\n3. Scissors")
        user_choice = int(input("Enter your choice: "))
        while user_choice < 1 or user_choice > 3:
            user_choice = int(input("Enter a valid choice: "))
        return self.items[user_choice]

    def get_computer_choice(self):
        computer_choice = random.randint(1, 3)
        return self.items[computer_choice]

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "It's a tie"
        elif self.winners[self.user_choice] == self.computer_choice:
            return "User wins"
        else:
            return "Computer wins"

    def play(self):
        self.user_choice = self.get_user_choice()
        self.computer_choice = self.get_computer_choice()
        print("User choice:", self.user_choice)
        print("Computer choice:", self.computer_choice)
        print(self.determine_winner())

if __name__ == "__main__":
    game = Game()
    game.play()