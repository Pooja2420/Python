# Start of Program of Goldbach's Conjecture for all integers less than 100
# Function to generate all primes up to n using a sieve of Eratosthenes
# Defining is_prime_sieve() function to find the number is prime or not
def is_prime_sieve(n): 
    # Creating a list of booleans n values set to True
    primes = [True] * (n + 1) 
    # Setting the n[0] and n[1] to False as 1 and 0 are not prime
    primes[0] = primes[1] = False 
    # Iterating from 2 to the square root of n +1
    for i in range(2, int(n**0.5) + 1): 
        # If i is prime, mark all its multiples as False
        if primes[i]: 
            for j in range(i * i, n + 1, i):
                primes[j] = False
    # Returning the list of booleans in a list primes
    return primes 

# Defining GoldBach() function to test Goldbach's Conjecture for a given even number from 1 to 100
def GoldBach(n): 
    # if n is less than or equal to 2 or odd, it is not valid since it 1 is not a prime number
    if n <= 2 or n % 2 != 0: 
        print("Invalid input")
        return
    # generate all primes up to n using the sieve function
    primes = is_prime_sieve(n)
    # Iterating from 2 to n-1 index numbers
    for p in range(2, n): 
        # checking if p and n-p are both prime using the list of booleans
        if primes[p] and primes[n - p]: 
            # Printing sum of two primes
            print(n, "=", p, "+", n - p) 
            # Return is used to break the if condition instead of printing the no solution message until the iteration of num reaches 100
            return
    # If no solution is found, print the below message
    print("No solution found") 

def main():
    # iterate from 4 to 100 with a step of 2
    for num in range(4,101,2): 
        # call the goldbach function for each even number
        GoldBach(num) 
main()
