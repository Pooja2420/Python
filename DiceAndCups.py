
# Importing random module to generate random numbers when the dices are being rolled.
import random

# Creating a parent class sixSidedDie.
class SixSidedDie:
    
    # Creating a method __init__ with parameter of instance self to access the faceValue attribute.
    def __init__(self):
        # Initializing faceValue = 1 since the die does not have 0 or negatives.
        self.faceValue = 1

    # Creating a method roll() with parameter of instance self to access the faceValue attribute.
    def roll(self):
        # Generating faceValue with random numbers from 1 to 6 since its a six sided die.
        self.faceValue = random.randint(1, 6)
        # Returning the random value generated in roll() function.
        return self.faceValue

    # Creating getFaceValue method with parameter of instance self to access the faceValue attribute.
    def getFaceValue(self):
        # Returns the value of the instance variable faceValue of the current object.
        return self.faceValue

    # Creating __repr__ method with parameter of instance self.
    def __repr__(self):
       # Returns a string representation of the six sided die.
        return f"SixSidedDie({self.faceValue})"
    
# Creating a child class TenSidedDie inheriting all attributes and methods of the SixSidedDie.
class TenSidedDie(SixSidedDie):
    
    # Creating a method roll() with parameter of instance self to access the faceValue attribute.
    # Overriding roll method to provide their own implementation.
    def roll(self):
        # Generating faceValue with random numbers from 1 to 10 since its a ten sided die.
        self.faceValue = random.randint(1, 10)
        # Returns the value of the instance variable faceValue of the current object.
        return self.faceValue

    # Creating __repr__ method with parameter of instance self.
    # Overriding __repr__ method to provide their own implementation.
    def __repr__(self):
        # Returns a string representation of the ten sided die.
        return f"TenSidedDie({self.faceValue})"

# Creating a child class TwentySidedDie inheriting all attributes and methods of the SixSidedDie. 
class TwentySidedDie(SixSidedDie):
    
     # Creating a method roll() with parameter of instance self to access the faceValue attribute.
     # Overriding roll method to provide their own implementation.
    def roll(self):
        # Generating faceValue with random numbers from 1 to 6 since its a twenty sided die.
        self.faceValue = random.randint(1, 20)
        # Returns the value of the instance variable faceValue of the current object.
        return self.faceValue

    # Creating __repr__ method with parameter of instance self.
    # Overriding __repr__ method to provide their own implementation.
    def __repr__(self):
        # Returns a string representation of the twenty sided die.
        return f"TwentySidedDie({self.faceValue})"

# Creating a cup class containing multiple dice.
class Cup:
    
    # Creating __init__ method which takes three arguments (six, ten and twenty) and parameter of instance self.
    def __init__(self, six=1, ten=1, twenty=1):
        # Initializing dice attribute. 
        self.dice = [SixSidedDie() for _ in range(six)] + [TenSidedDie() for _ in range(ten)] + [TwentySidedDie() for _ in range(twenty)]
        # Initializing sum attribute.
        self.sum = sum(die.getFaceValue() for die in self.dice)

    # Creating roll method which rolls all dice in the cup. The `getSum` method returns the current sum of face values of all dice in the cup. The `__repr__` method returns a string representation of the cup.
    def roll(self):
        # Updating the sum after the rolls.
        self.sum = sum(die.roll() for die in self.dice)
        # Returns the updated sum to roll method.
        return self.sum

    # Creating getSum method with parameter of instance self.
    def getSum(self):
        # Returns the current sum of face values of all dice in the cup
        return self.sum

    # Creating __repr__ method with parameter of instance self.
    def __repr__(self):
        # Returns  string representation of the cup.
        return "Cup(" + ",".join(str(die) for die in self.dice) + ")"

# Creating main function to start the execution of the code.
def Main():
    # Passing the number of six, ten and twenty sided dice.
    six = int(input("Number of Six sided dice to roll : "))
    ten = int(input("Number of Ten sided dice to roll : "))
    twenty = int(input("Number of Twenty sided dice to roll : "))
    # Calling the cup class according to the user’s input.
    cup=Cup(six,ten,twenty)
    # Rolling the cups. 
    print(cup.roll())
    # Getting the sum of the cups.
    print(cup.getSum())
    # Printing the rolles and sum value according to number of six, ten and twenty sided dice.
    print(cup)
# Calling the main function to execute the program.
Main()




