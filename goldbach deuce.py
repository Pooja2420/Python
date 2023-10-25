# Function to perform binary search on a lst
def binary_search(lst, target):
    # Initializing left and right pointers staring from 0 to length of lst - 1
    left = 0
    right = len(lst) - 1

    # Looping until left is greater than right pointer
    while left <= right:
        # If found find the middle index
        mid = (left + right) // 2

        # If target is found, return True
        if lst[mid] == target:
            return True

        # If target is small than the middle element, move the right pointer to the left of the middle index
        elif target < lst[mid]:
            right = mid - 1

        # If target is large than the middle element, move the left pointer to the right of the middle index
        else:
            left = mid + 1

    # If target is not found, return False
    return False

import random
def main():
# Getting inputs from user for n and sum
    n = int(input("Enter the number of values in the list: "))
    sum = int(input("Enter sum: "))

# Creating a sorted list of n random numbers between 0 and 100
    lst = sorted([random.randint(0, 100) for _ in range(n)])
    print (lst)

# Initializing a boolean flag to false
    found = False

# Initializing two variables to store the two numbers that makes the sum
    num1 = None
    num2 = None

# Loop through the list
    for i in range(n):
        # Finding the complement of the current element to perform binary search
        complement = sum - lst[i]
    
        # Performing binary search 
        if binary_search(lst[i+1:], complement):
            # If found, set the flag to True 
            found = True
            # Store the two element in num1 and num2
            num1 = lst[i]
            num2 = complement
            # Breaking the loop if the sum is found
            break

# Output for the results
    if found:
        print(f"Yes, there are two numbers in list that sum to {sum}.")
        # Print num1 and num2 using a formatted string
        print(f"The two numbers are {num1} and {num2}.")
    else:
        print(f"No, there are no two numbers in {lst} that sum to {sum}.")

main()
