# Python code to check if a number is a happy prime, sad prime, happy non-prime, or sad non-prime.
# Defining the is_happy() function to check if a number is happy or not
def is_happy(n):
    # Creating an empty set to store the visited numbers 
    visited = set() 
    # Looping until n becomes 1. If n becomes one the it is happy prime or happy non-prime
    if len(str(n)) > 1:
        while n != 1: 
        # Replacing n by the sum of the square of its digits
            n = sum(int(i)**2 for i in str(n)) 
        # If n is already in the set, it means there is a cycle and n is not happy
            if n in visited: 
                return False
            # otherwise, add n to the set
            visited.add(n)
    elif n==1:
        return True
    else:
        visited.add(n)
        return False 
    # If n(iteration of sum of digits) becomes 1, it is happy
    return True 

# Defining is_prime() function to check if a number is prime or not
def is_prime(n):
    # If n is less than or equal to 1, it is not a prime number
    if n <= 1: 
        return False
    # Iterating from 2 to the square root of n numbers
    for i in range(2, int(n**0.5) + 1): 
        # If n is divisible by i(any number), then it is not prime number 
        if n % i == 0: 
            return False
    # Otherwise returning it is prime number
    return True 

# Defining the main() function to get inputs from user and deciding whether happ/sad prime and happy/sad non-prime numbers and for exception handling.
def main():
    # Creating an endless loop that requests/accepts an integer from the user
    while True:
        try:
        # Requesting input from the user
            num = int(input("Enter a number: ")) 
        # Checking if the input is a happy prime
            if is_happy(num) and is_prime(num): 
                print(num, "is a happy prime")
        # Checking if the input is a sad prime
            elif not is_happy(num) and is_prime(num): 
                print(num, "is a sad prime")
        # Checking if the input is a happy non-prime
            elif is_happy(num) and not is_prime(num): 
                print(num, "is a happy non-prime")
        # Otherwise checking if the input number is a sad non-prime
            else: 
                print(num, "is a sad non-prime")
        # If the input is not an integer, printing an error message
        except ValueError:  
            print("Invalid input. Please enter a positive integer.")

# Calling the main function to start with the execution of the program
main()
