# Importing required Modules.
import random
# Creating SimplePlotGenerator class for generating simple plots.
class SimplePlotGenerator:
    # Creating constructor method.
    def __init__(self):
        # Initializing the return value.
        self.return_value = 'Something happens'
    
    # Creating printer method to print.
    def printer(self):
        return self.return_value

# Creating RandomPlotGenerator class with extended SimplePlotGenerator class.
class RandomPlotGenerator(SimplePlotGenerator):
    # Creating the constructor method.
    def __init__(self):
        # Initializing names from text file.
        self.name = [name for name in open('plot_names.txt').read().split('\n') if name != '']
        # Initializing adjectives from text file.
        self.adjectives = [adj for adj in open('plot_adjectives.txt').read().split('\n') if adj != '']
        # Initializing professions from text file.
        self.professions = [prof.strip() for prof in open('plot_profesions.txt').read().split('\n') if prof !='']
        # Initializing verbs from text file.
        self.verbs = [verb for verb in open('plot_verbs.txt').read().split('\n') if verb != '']
        # Initializing evil adjectives from text file.
        self.adjectives_evil = [adj_e for adj_e in open('plot_adjectives_evil.txt').read().split('\n') if adj_e != '']
        # Initializing villain jobs from text file.
        self.villian_job = [villian_job for villian_job in open('plot_villian_job.txt').read().split('\n') if villian_job != '']
        # Initializing villains from text file.
        self.villians = [villian for villian in open('plot_villains.txt').read().split('\n') if villian != '']
    
    # Creating printer method to print.
    def printer(self):
       # Generating random plots.
       self.return_value = random.choice(self.name) + ', a ' + random.choice(self.adjectives) + ' ' + random.choice(self.professions) + ', must ' + random.choice(self.verbs) + ' the ' + random.choice(self.adjectives_evil) + ' ' + random.choice(self.villian_job) + ', ' + random.choice(self.villians) + '.'
       return self.return_value

# Creating InteractivePlotGenerator class with extended SimplePlotGenerator class.
class InteractivePlotGenerator(SimplePlotGenerator):
    # Creating the constructor method.
    def __init__(self):
        # Initializing names from text file.
        self.name = [name for name in open('plot_names.txt').read().split('\n') if name != '']
        # Initializing adjectives from text file.
        self.adjectives = [adj for adj in open('plot_adjectives.txt').read().split('\n') if adj != '']
        # Initializing professions from text file.
        self.professions = [prof.strip() for prof in open('plot_profesions.txt').read().split('\n') if prof !='']
        # Initializing verbs from text file.
        self.verbs = [verb for verb in open('plot_verbs.txt').read().split('\n') if verb != '']
        # Initializing evil adjectives from text file.
        self.adjectives_evil = [adj_e for adj_e in open('plot_adjectives_evil.txt').read().split('\n') if adj_e != '']
        # Initializing villain jobs from text file.
        self.villian_job = [villian_job for villian_job in open('plot_villian_job.txt').read().split('\n') if villian_job != '']
        # Initializing villains from text file.
        self.villians = [villian for villian in open('plot_villains.txt').read().split('\n') if villian != '']        
        # Printing instructions for the user.
        print('\nEnter number 1-5 that corresponds to your choice of word.\n')
        print('This happens 7 times to generate plot.\n')


    def Input_Checker(self, random_5):
        # Checking for valid inputs given by the user.
        while True:
            try:
                print('List of 5 random selections')
                print(random_5, '\n')
                user_select = int(input('Enter user selection from 1 to 5: '))
                if user_select == 1:
                    return random_5[0]
                elif user_select == 2:
                    return random_5[1]
                elif user_select == 3:
                    return random_5[2]
                elif user_select == 4:
                    return random_5[3]
                elif user_select == 5:
                    return random_5[4]                
                else:
                    print('Enter a number 1-5 please.')
            except:
                print('Invalid Input')
    
    def printer(self):
        # Randomly selecting 5 names.
        name_5 = random.sample(self.name, 5)
        self.pick_name = self.Input_Checker(name_5)
        
        # Randomly selecting 5 adjectives.
        adj_5 = random.sample(self.adjectives, 5)
        self.pick_adj = self.Input_Checker(adj_5)
        
        # Randomly selecting 5 professions.
        prof_5 = random.sample(self.professions, 5)
        self.pick_prof = self.Input_Checker(prof_5)
        
        # Randomly selecting 5 verbs.
        verb_5 = random.sample(self.verbs, 5)
        self.pick_verb = self.Input_Checker(verb_5)
        
        # Randomly selecting 5 evil adjectives.
        adj_e_5 = random.sample(self.adjectives_evil, 5)
        self.pick_adj_e = self.Input_Checker(adj_e_5)
        
        # Randomly selecting 5 villain jobs.
        villian_job_5 = random.sample(self.villian_job, 5)
        self.pick_villian_job = self.Input_Checker(villian_job_5)
        
        # Randomly selecting 5 villains.
        villian_5 = random.sample(self.villians, 5)
        self.pick_villians = self.Input_Checker(villian_5)
        
        # Generating plot according to user's choices
        self.return_value = self.pick_name + ', a ' + self.pick_adj + ' ' + self.pick_prof + ', must ' + self.pick_verb + ' the ' + self.pick_adj_e + ' ' + self.pick_villian_job + ', ' + self.pick_villians + '.'
        return self.return_value


class PlotViewer:
    # Creating method to register a plot generator
    def register_plot_generator(self, generator):
        self.print_sub = generator

    # Creating method to print the plot.
    def printer(self):
        return self.print_sub.printer()

# Creating main function to execute the code.
def main():  
    pv = PlotViewer()
    pv.register_plot_generator(SimplePlotGenerator())
    print("\nSimple:\n{}".format(pv.printer()))
    
    pv.register_plot_generator(RandomPlotGenerator())
    print("\nRandom:\n{}".format(pv.printer()))
    
    pv.register_plot_generator(InteractivePlotGenerator())
    print("\nInteractive:\n{}".format(pv.printer()))

# Calling the main function to start the execution of code.
main()

    
