# Name: Pooja Venugopal Baskaran
# Date : 15 November 2023
# Honour Statement: I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://www.youtube.com/watch?v=LDnRxqwmz8U

# Importing required modules.
import numpy as np
import random

# Creating conway function with size and probability parameters.
def conway(s, p):
    # Creating a list of 1s and 0s.
    numlist = []

    # Calculating total number of cells.
    total_cells = s**2

    # Calculating number of cells to be alive based on the probability.
    alive_cells = round(total_cells * p)

    # Generating dead cells.
    for _ in range(total_cells - alive_cells):
        numlist.append(0)

    # Generating alive cells.
    for _ in range(alive_cells):
        numlist.append(1)

    # Shuffling list to randomize the cell positions.
    random.shuffle(numlist)

    # Converting the list into a 2D array using reshape function.
    board = np.asarray(numlist).reshape(s, s)
    print(board)
    return board

# CReating advance function with board and advances t times step as parameters.
def advance(b, t):
    # Advancing board state for t time steps.
    for _ in range(t):
        # Adding pad to the board
        b = np.pad(b, pad_width=1, mode='constant', constant_values=0)

        # Creating new list for the updated board state.
        new_board_state = []

        # Getting size of the board.
        size = b.shape[0]

        # Iterating over each cell in the board.
        for i in range(1, size):
            for j in range(1, size):
                # Applying rules as mentioned in the pdf.
                if b[i][j] == 0:
                    try:
                        # Counting number of alive neighbors.
                        alive_neighbors = b[i-1][j] + b[i+1][j] + b[i][j-1] + b[i][j+1]

                        # If a dead cell has exactly 3 alive neighbors, it becomes alive.
                        if alive_neighbors == 3:
                            new_board_state.append(1)
                        else:
                            new_board_state.append(0)
                    except:
                        pass
                elif b[i][j] == 1:
                    try:
                        # Counting number of alive neighbors.
                        alive_neighbors = b[i-1][j] + b[i+1][j] + b[i][j-1] + b[i][j+1]

                        # If an alive cell has 2 or 3 alive neighbors, it stays alive
                        # Otherwise, it dies
                        if 2 <= alive_neighbors <= 3:
                            new_board_state.append(1)
                        else:
                            new_board_state.append(0)
                    except:
                        pass

        # Updating board state.
        b = np.asarray(new_board_state).reshape(size-2, size-2)
        print(b)
    print(b)

# Creating main function to start the execution of the code.
def main():
    size=int(input("Enter size of array : "))
    probability = float(input("Enter the probability : "))
    t_step=int(input("enter the number of steps to be advanced : "))
    # Creating board and advance its state.
    board = conway(size,probability)
    advance(board, t_step)
# Caliing main function to start execution of the program.
main()
