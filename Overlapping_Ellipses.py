# Name: Pooja Venugopal Baskaran
# Date : 04 November 2023
# Honour Statement: I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://www.youtube.com/watch?v=pBjJ7_KuOJ0

# Importing datetime module from datetime library for date and time manipulations
from datetime import datetime  
# Importing specific functions from a custom module named 'WarAndPeace'
from WarAndPeace import get_Char, group_Char,bin,WarAndPeacePseudoRandomNumberGenerator,greater_Than,get_Score  # Importing specific functions from a custom module named 'WarAndPeace'
# Importing math module for mathematical operations
import math  

# Creating Point class.
class Point:  
    # Creating __init__ constructor method for the class.
    def __init__(self, x_coord=0, y_coord=0):  
        # Assigning the inputs.
        self.x_coord = x_coord   
        self.y_coord = y_coord  

    # Creating set_x method to set co-ordinates of x.
    def set_x(self, x_coord):  
        self.x_coord = x_coord  

     # Creating set_y method to set co-ordinates of y.
    def set_y(self, y_coord):  
        self.y_coord = y_coord  

    # Creating distance method to calculate distance between points.
    def distance(self, point):  
        return math.sqrt((self.x_coord - point.x_coord) ** 2 + (self.y_coord - point.y_coord) ** 2)  

    # Creating get_coord method to get co-ordinates.
    def get_coord(self):  
        return (self.x_coord, self.y_coord)  

# Creating Ellipse class.
class Ellipse:  
    # Creating constructor method.
    def __init__(self, p1, p2, width): 
        # Assigning p1 and p2.
        self.p1 = p1  
        self.p2 = p2  
        # Getting Co-ordinates of p1 and p2.
        self.x1, self.y1 = p1.get_coord()  
        self.x2, self.y2 = p2.get_coord() 
        # Assigning width to instance variable.
        self.major_axis = width 

    # CReating ellipse_value method.
    def ellipse_value(self):  
        # Calculating distance.
        self.dist_e = ((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2) ** (1 / 2)
        self.half_major_axis = self.major_axis / 2  
        self.half_dis = self.dist_e / 2  
        # Calculating minor axis using Pythagorean theorem.
        self.minor_axis = math.sqrt((self.major_axis ** 2) - (self.dist_e ** 2))  
        self.half_minor_axis = self.minor_axis / 2 

    # Creating focal_Distance method.
    def focal_Distance(self):
        return self.dist_e  

    # Creating box_Bounding method.
    def box_Bounding(self):  
        return self.major_axis * self.half_minor_axis  

    # Creating inside_ellipse method.
    def inside_ellipse(self, point):  
         # Calculating the sum of the distances
        dist = point.distance(self.p1) + point.distance(self.p2)  
        return dist <= self.major_axis  

# Creating Elipse_Simulator function.
def Elipse_Simulator(seed, x_max, x_min, y_max, y_min, e1, e2, rand_point):
    # Initializing the count = 0.
    countInEllipse = 0 
    total_points = 0

    # Calling the pseudo random number generator with the given seed from WarAndPeace python code.
    prng = WarAndPeacePseudoRandomNumberGenerator(seed)  
    # Looping the number of random points.
    for num in range(rand_point):
        # Generating random for x coordinate.
        x_cor = (x_max - x_min) * prng.random() + x_min

        # Generating random for y coordinate.
        y_cor = (y_max - y_min) * prng.random() + y_min
        point_rand = Point(x_cor, y_cor)
        if e1.inside_ellipse(point_rand) and e2.inside_ellipse(point_rand):
            countInEllipse += 1
        total_points += 1
    return (countInEllipse, total_points)

# Creating box class.
class box:
    # Creating constructor method.
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    # Creating x_value method.
    def x_value(self):
        max_width = max(self.e1.major_axis, self.e2.major_axis)
        x_coor = [self.e1.x1, self.e1.x2, self.e2.x1, self.e2.x2]
        self.x_min = min(x_coor) - max_width / 2
        self.x_max = max(x_coor) + max_width / 2

    # Creating y_value method.
    def y_value(self):
        max_width = max(self.e1.major_axis, self.e2.major_axis)
        y_coor = [self.e1.y1, self.e1.y2, self.e2.y1, self.e2.y2]
        self.y_min = min(y_coor) - max_width / 2
        self.y_max = max(y_coor) + max_width / 2

    # Creating get_value method.
    def get_value(self):
        return self.x_min, self.x_max, self.y_min, self.y_max

    # Creating Area_Of_Box method.
    def Area_Of_Box(self):
        return (self.x_max - self.x_min) * (self.y_max - self.y_min)
# Creating input_For_Elipses function to get the inputs for the overlapping area of ellipses.
def input_For_Elipses():
    p1_e1_x = int(input('Enter Point1 X for Ellipse 1: '))
    p1_e1_y = int(input('Enter Point1 Y for Ellipse 1: '))
    p2_e1_x = int(input('Enter Point2 X for Ellipse 1: '))
    p2_e1_y = int(input('Enter Point2 Y for Ellipse 1: '))

    p1_e2_x = int(input('Enter Point1 X for Ellipse 2: '))
    p1_e2_y = int(input('Enter Point1 Y for Ellipse 2: '))
    p2_e2_x = int(input('Enter Point2 X for Ellipse 2: '))
    p2_e2_y = int(input('Enter Point2 Y for Ellipse 2: '))

   # Creating Error Handling.
    p1_e1 = Point(p1_e1_x, p1_e1_y)
    p2_e1 = Point(p2_e1_x, p2_e1_y)

    p1_e2 = Point(p1_e2_x, p1_e2_y)
    p2_e2 = Point(p2_e2_x, p2_e2_y)
    while True:
        try:
            width_e1 = int(input('Select Width for Ellipse 1:'))
            width_e2 = int(input('Select Width for Ellipse 2: '))
            e1 = Ellipse(p1_e1, p2_e1, width_e1)
            e2 = Ellipse(p1_e2, p2_e2, width_e2)
            e1_val = e1.ellipse_value()  
            e2_val = e2.ellipse_value()  
            if width_e1 < e1.focal_Distance() or width_e2 < e2.focal_Distance():
                print('This Width is so small! Try some high value')
            else:
                return p1_e1_x, p1_e1_y, p2_e1_x, p2_e1_y, p1_e2_x, p1_e2_y, p2_e2_x, p2_e2_y, width_e1, width_e2
        except ValueError:
            print('Enter another right Value.')

# Creating compute_Overlapping_Of_Ellipses function.
def compute_Overlapping_Of_Ellipses(e1, e2, rand_point, seed):
    # Getting the bounding box of two ellipses.
    box_Bounding = box(e1, e2)
    # Getting x and y values of the bounding box.
    x_value = box_Bounding.x_value()  
    y_value = box_Bounding.y_value()
    # Getting minimum and maximum x and y values.
    x_min, x_max, y_min, y_max = box_Bounding.get_value()
    # Getting the count of points inside the ellipses and the total points using the Elipse_Simulator function.
    point, total = Elipse_Simulator(seed, x_max, x_min, y_max, y_min, e1, e2, rand_point)
    return box_Bounding.Area_Of_Box() * (point/total)

# Creatimg main function to execute the program.
def main():
    px1_e1, px2_e1, py1_e1, py2_e1, px1_e2, px2_e2, py1_e2, py2_e2, w_e1, w_e2 = input_For_Elipses()
    p1_e1 = Point(px1_e1, py1_e1)
    p2_e1 = Point(px2_e1, py2_e1)

    p1_e2 = Point(px1_e2, py1_e2)
    p2_e2 = Point(px2_e2, py2_e2)

    e1 = Ellipse(p1_e1, p2_e1, w_e1)
    e2 = Ellipse(p1_e2, p2_e2, w_e2)
    # Getting seed value.
    seed = int(input('Enter the seed Number :'))
    # Getting number of random points.
    num_rand = int(input('Enter number of random points on elipse: '))
    # Printing the area of overlapping ellipses.
    print('Area of overlapping Ellipses', compute_Overlapping_Of_Ellipses(e1, e2, num_rand, seed))
    
# Calling main function to start the execution of the code.
main()