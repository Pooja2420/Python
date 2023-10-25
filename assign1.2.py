def Computegcd(num1, num2): # initializing a function for gcd computation
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def is_coprime(x, y):    # initializing a function for checking gcd==1 for coprime computation
    return Computegcd(x, y) == 1
# getting inputs to compute co-prime
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if is_coprime(num1, num2):
    print(num1, "and", num2, "are coprime")
else:
    print(num1, "and", num2, "are not coprime")



    
