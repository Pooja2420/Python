# Start of the program
# Function for reading a txt file
def read_file(file_path):
    with open(file_path, 'rb') as file:
        file = [int(line.strip()) for line in file]
    return file

# Function for Stem and leaf plot
def stemplot(data):
   # Determine the number of digits in the largest number
    maximum = len(str(max(data)))
    # Define stem and leaf places based on max_digits
    place = 10 ** (maximum - 1)
    # Creating empty dictionary to store the stems and leaf as key value pairs
    StemPlot = {}
    # Looping through each number in the data
    for i in data:
        # Calculate the stem and leaf using divmod 
        stem, leaf = divmod(i, 10)
        # Add leaf to the appropriate stem in the dictionary as a key value pair
        if stem in StemPlot:
            StemPlot[stem].append(leaf)
        else:
            StemPlot[stem] = [leaf]
    # Print the stem-and-leaf plot
    for stem in sorted(StemPlot.keys()):
        print(f"{stem}: {' '.join(map(str, sorted(StemPlot[stem])))}")
# Function for switch case
def switch(case):
    # Creating dictionary to store the input received from user to call that file where keys are cases, values are file paths
    switch_dict = {
        '1': 'D:/DSC_430/assign 2/StemAndLeaf1.txt',
        '2': 'D:/DSC_430/assign 2/StemAndLeaf2.txt',
        '3': 'D:/DSC_430/assign 2/StemAndLeaf3.txt'
    }
    # Getting a value from dictionary using key 
    # Having switch_dict.get(case) as reference and calling switch function
    file_path = switch_dict.get(case)
    if file_path is not None:
        data = read_file(file_path)
        stemplot(data)
    else:
        print("Invalid file number")
def main():
    while True:
        Greet = "Hello User! Welcome to steam and leaf plot python Code"
        print(Greet)
        case = input("Enter a case 1, 2, 3 or 'exit' to quit: ")
        if case == "exit":
            print("The code is quit by the user")
            break
        switch(case)
main()
