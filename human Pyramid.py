# Function creation for human pyramid.
def humanPyramid(row, column):
    # Initialising the value of weight as mentioned in the assignment
    weight = 128
    # Base cases: Rows and colums should not be negative and columns should not be greater that rows.
    if row < 0 or column < 0 or column > row:
        return 0
    # Recursion cases: sum of their own weight plus half of weights above as mentioned in the inputs.
    return weight + (humanPyramid(row - 1, column - 1) + humanPyramid(row - 1, column)) / 2
    

# Function creation for main method.
def Main():

    # Taking inputs for row, column and weight from the user.
    r = int(input("Enter number of rows : "))
    c = int(input("Enter number of columns : "))
    weight = 128

    # Calling human pyramid function to print the extra value carried on that person back in humanPyramid function
    print (humanPyramid(r,c)-weight)

# Calling the main function to start execution of the program.
Main()
