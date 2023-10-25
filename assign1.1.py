# Name: Pooja Venugopal Baskaran
# Date : 15 September 2023
# I have not given or received any unauthorized assistance on this assignment.

def GradeLogic(): #defining the grading logic function. It performs the logic for grading.
    value_1=str(input("Assignment submitted? (Yes/No)"))
    grade=0   # initializing grade as zero
    if (value_1=="No"):
        print ("The  assignment is not submitted, so grade is 0")
    else:
        value_2=str(input("Is the name and date included in the assignment? (Yes/No)"))
        if (value_2=="No"):
            print ("No name and date in the assignment, so the grade is 0")
        else:
            value_3=str(input("Is the honor statement included in the assignment? (Yes/No)"))
            if (value_3=="No"):
                print("No honor statement in the assignment, so the grade is 0")
            else:
                value_4=str(input("Did you include a short video on explaining the assignment? (Yes/No)"))
                if(value_4=="No"):
                    print("Since no expaination video is available the grade is 0")
                else:
                    value_5=int(input("How will you evaluate the correctness of the code on the scale of 10 ?"))
                    grade+=value_5
                    value_6=int(input("How will you rate the elegance of the code on the scaleo of 10 ?"))
                    grade+=value_6
                    value_7=int(input("How will you rate the code hygiene of the code on the scaleo of 10 ?"))
                    grade+=value_7
                    value_8=int(input("How will you rate the quality of the code on the scaleo of 10 ?"))
                    grade+=value_8
                    value_9=str(input("Have submitted the asignment before the deadline? (Yes/No)"))
                    if(value_9=="No"):
                        value_10=int(input("How many hours after the deadline the code was submitted?"))   
                        grade=grade-(grade+value_10)//100    #Evaluating grade based on the above criterias. Subracting the hours as 1hr = 1 mark
                    print("Your assignment score is ",grade,"/40")

GradeLogic()

        
            

