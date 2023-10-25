# Name: Pooja Venugopal Baskaran
# Date : 19 October 2023
# Honour Statement: I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://youtu.be/J8qytrcn3KI

# Importing random module to generate random numbers when the dices are being rolled.
import random
# Importing classes that are used in Dice and Cups assignment.
# Importing only cup class since that class takes arguments from six, tenand twenty sided dice
from DiceAndCups import Cup

# Creating the greet class to greet and get user's name.
class Greet():
    # Creating a __init__ with parameter of instance self to access the name, balance and play attribute.
    def __init__(self):
        # Greeting the user ansking their name.
        self.name = input("Welcome to the Cup and Dice game! What is your name? ")
        # Setting the balance of that custoner to $100.
        self.balance = 100
        # Asking if the user if he/she likes to play a game.
        print(f"Welcome, {self.name}! You have a balance of ${self.balance}. Do you like to play a game? (yes/no)")
        # Case changing to lower since the while lop only checks lower cases.
        self.play = input().lower()

    # Creating a CupsAndDice metho with parameter of instance self to access the attributes inside this class.
    def CupsAndDice(self):
        # Checking the user's answer.
        while self.play == 'yes':
            # if the balance is less than 0, print not enough balance
            if self.balance <= 0:
                print("You don't have enough balance to play again.")
                break
            # Generating random numbers from 1 to 100 andsetting it has goal.
            self.goal = random.randint(1, 100)
            print(f"Goal is {self.goal}.")
            # For improper betting cases.
            while True:
                # Asking the user for the bet amount and assigning to bet variable.
                self.bet = int(input("How much do you want to bet?"))
                # If bet is negative or zero.
                if self.bet <= 0:
                    print("Bet should be more than 0.")
                # If bet is more than balance.
                elif self.bet > self.balance :
                    print("You cannot bet more than your current balance.")
                else:
                    break            
            # Deducting bet amount from balance and updating the balance amount.
            self.balance -= self.bet
            # Asking the user the number of each dice to roll since cup class has three classes.
        
            six = int(input("Number of Six sided dice to roll : "))
            ten = int(input("Number of Ten sided dice to roll : "))
            twenty = int(input("Number of Twenty sided dice to roll : "))
            # Calling the cup class according to the user’s input.
            cup = Cup(six, ten, twenty)
            # Calling the roll method for cup class.
            roll = cup.roll()
            # Displying the rolled random value.
            print(f"You rolled a {roll}.")
            # Checking the roll value and goal value is same.
            if roll == self.goal:
                #  If the roll exactly matches the goal, the user receives 10x bet added to their balance.
                self.balance += 10 * self.bet
                print(f"Congratulations! You hit the goal and won ${10*self.bet}!")
            # If the roll is within 3 of the goal but not over, the user receives 5x bet added to their balance.
            elif roll <= self.goal and roll >= self.goal - 3:
                self.balance += 5 * self.bet
                print(f"You were so close to the goal and won ${5*self.bet}!")
            # If the roll is within 10 of the goal but not over, the user receives 2x bet added to their balance.
            elif roll <= self.goal and roll >= self.goal - 10:
                self.balance += 2 * self.bet
                print(f"You are almost close to the goal and won ${2*self.bet}!")
            else:
                print("Sorry! Not even close to the goal. Better luck next time!")
            # Ask the user if they would like to play again.
            print(f"{self.name}, your updated balance is ${self.balance}. Would you like to play again? (yes/no)")
            self.play = input().lower()
        # If user is not willing end the game.
        print("Thanks for playing!")

# Creating main function to execute the code.
def main():
    game = Greet()
    game.CupsAndDice()

# Calling main function to start the execution of the code.
main()
