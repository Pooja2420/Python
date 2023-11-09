# Name: Pooja Venugopal Baskaran
# Date : 04 November 2023
# Honour Statement: I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://www.youtube.com/watch?v=MnF1ZNTVIkY


# Importing required module
from datetime import datetime 
import random
import numpy as np
# Defining a WarAndPeacePseudoRandomNumberGenerator class.
class WarAndPeacePseudoRandomNumberGenerator():
    # Creating constructor method.
    def __init__(self, seed = None):
        # If no seed is provided, generate a seed
        self.seed = seed if seed else self.generate_seed()

    # Creating generate_seed method.
    def generate_seed(self):
        # Getting the current timestamp.
        seed = str(datetime.now().timestamp())
        # Removing the decimal point.
        seed = seed.replace('.', '')[-5:]
        # Converting the string back to an integer.
        return int(seed)

    # Creating radom method to generate a random number.
    def random(self):
        # Calling the bin method with the current seed.
        r = bin(self.seed)
        return r

# Defining getChar function.
def get_Char(file, seed):
    # Initializing empty list to store characters.
    charList = []
    # Initializing counter variable.
    x = 0 
    # Opening the file in read mode.
    with open(file) as f:
        # Looping until the counter reaches 64.
        while x < 64:
            # Moving the file pointer specified seed position.
            f.seek(seed)
            char = f.read(1)
            if x > 0:
                if char == charList[-1]:
                    seed = seed + 1
                    f.seek(seed)
                    char = f.read(1)
                    # If the character is also the same as the last one in the list.
                    if char == charList[-1]:
                        # Incrementing the seed.
                        seed = seed +1
                        # Moving the file pointer to the new position.
                        f.seek(seed)
                        # Reading another new character from the file.
                        char = f.read(1)
                        # Adding this character to the list.
                        charList.append(char)
                    else:
                        # If this character is different, adding it to list directly.
                        charList.append(char)
                else:
                    charList.append(char)
            else:
                # adding the character to the list directly if it is the first iteration of the loop.
                charList.append(char)
            # Incrementing the seed by 100.
            seed = seed + 100
            # Incrementing the counter variable.
            x = x + 1
    return charList 

# Defining groupChar function.
def group_Char(charList):
    # Setting group size to 2.
    n = 2
    # Creating a new list where each element is a sublist of n characters from the original list.
    newCharList = [(charList[i:i+n]) for i in range(0, len(charList), n)]
    return newCharList

# Define greaterThan function.
def greater_Than(newCharList):
    # Initializing an empty list.
    score = []
    # Looping over each group of characters in the list.
    for i in newCharList:
        if i[0] > i[1]:
            # Appendding 1 to the score list.
            score.append(1)
        elif i[0] < i[1]:
            # Appendding 0 to the score list
            score.append(0)
    return score
            
# Defining getScore function.
def get_Score(score):
    # Initializing variable to store the result.
    r = 0
    # Initializing counter variable.
    n = 0
    for i in score:
        n = n + 1
        # Adding to result the current score times 1 divided by 2 to the power of the counter variable
        r = r + (i * (1/2**n))
    return r

# Creating empty list to store the results of each run of the bin method
results = []

# Creating bin method.
def bin(seed = 0):
    # Creating new instance of the PRNG class if no seed is provided. 
    if seed == 0:
        x = WarAndPeacePseudoRandomNumberGenerator()
        seed = x.generate_seed()
    # Open the text file and read characters based on the seed value
    file = 'war-and-peace.txt'
    charList = get_Char(file, seed)
    newCharList = group_Char(charList)
    score = greater_Than(newCharList)
    r = get_Score(score)
    # Appending r to results list.
    results.append(r)
    #print(r)
    return r

def Min_Max_Mean(seed,random_Points):
    random.seed(seed)
    results = [random.random() for _ in range(random_Points)]
    # Check if the list is empty
    if not results:
        return "Error: The list is empty."

    # Calculate the minimum, maximum, and mean values
    min_value = min(results)
    max_value = max(results)
    mean_value = np.mean(results)

    return min_value, max_value, mean_value

# Main function to start the program.
def Main():   
    # Asking the user for a seed input.  
    seed=int(input("Enter seed value: "))   
    prng_with_seed = WarAndPeacePseudoRandomNumberGenerator(seed)
    r_with_seed = prng_with_seed.random()
    print("The PRNG with seed is: ", r_with_seed)
    # Creating a PRNG without a specific seed
    prng = WarAndPeacePseudoRandomNumberGenerator()
    r = prng.random()
    print("The PRNG without seed is : ", r)
    random_Points=int(input("Enter number of random Points: "))
    min_value, max_value, mean_value = Min_Max_Mean(seed,random_Points)
    print("Min Value: ", min_value)
    print("Max Value: ", max_value)
    print("Mean Value: ", mean_value)

# Calling the main function to start the program.
Main()
