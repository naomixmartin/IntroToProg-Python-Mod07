# ------------------------------------------------------------------------ #
# Title: Assignment 07 -- Finding the Equation of a Line
# Description: Demonstrating Structured Error Handling and Pickling
#              This program acts as a basic calculator that allows the user
#              to find the equation of a linear line between two user-specified
#              points. The information is stored in a dictionary, and pickled.
# ChangeLog (Who,When,What):
# naomimartin, 08.22.2022, Created script and added code to complete assignment 07
# ------------------------------------------------------------------------ #

import math
import pickle

# ---- Data ---- #
mathDict = {}  # dictionary to hold calculated values
mathDictVar = None  # variable to hold each dictionary, so that each dictionary can be appended to list without overwriting previous values
mathDictList = []  # list to hold the dictionary for each run
strChoice = ""  # capture user option selection for menu
x1 = None  # define the x1 variable for user input
x2 = None  # define the x2 variable for user input
y1 = None  # define the y1 variable for user input
y2 = None  # define the y2 variable for user input
d = None  # define the variable to calculate the distance
m = None  # define the variable to calculate the slope
b = None  # define the variable to calculate the y-intercept
midx = None  # variable to hold the x value to calculate midpoint x value
midy = None  # variable to hold teh y value to calculate midpoint y value
x1Bln = None  # Boolean that when True will halt while loop in the function x1Input()
y1Bln = None  # Boolean that when True will halt while loop in the function y1Input()
x2Bln = None  # Boolean that when True will halt while loop in the function x2Input()
y2Bln = None  # Boolean that when True will halt while loop in the function y2Input()
binFile = None  # An object that represents a file
counter = 0  # counter #1 to count how many calculations, or dictionary objects, were saved to the list
i = 0  # counter #2 to iterate through lines of the specified file, so that all lines in the file can be unpickled
unpickled = None  # variable to hold the unpickled data

# ---- Processing ---- #

# Define most processing functions here: distance, slope, yint, midpoint

def distance(x_1, x_2, y_1, y_2):
    ''' Calculates the distance between two points. Exception handling not needed, as the possible exceptions
    ValueError, TypeError have been dealt with in the functions that receive user input for x1, x2, y1, y2.

    :param x_1: (float) with value for x1.
    :param x_2: (float) with value for x2.
    :param y_1: (float) with value for y1.
    :param y_2: (float) with value for y2.
    :return: (float) with calculated distance between two points
    '''

    d = math.sqrt((x_1 - x_2)**2 + (y_1-y_2)**2)
    print("\nDistance: the distance between the coordinates (%.2f, %.2f) and (%.2f, %.2f) is %.2f" % (x1, y1, x2, y2, d))
    return d

def slope(x_1, x_2, y_1, y_2):
    ''' Calculates the slope between two (x,y) coordinates. Need exception handling for the possible
        ZeroDivisionError exception.

    :param x_1: (float) with value for x1.
    :param x_2: (float) with value for x2.
    :param y_1: (float) with value for y1.
    :param y_2: (float) with value for y2.
    :return: (float) with value for slope 'm', or (string) with text if ZeroDivisionError exception is encountered.
    '''

    try:
        m = (y_2 - y_1) / (x_2 - x_1)
    except ZeroDivisionError as e:
        m = "INVALID DUE TO DIVISION BY ZERO"
        print("\nSlope: Invalid slope due to division by zero. Python's error message:", e)
    else:
        print("Slope: the slope of the line that joins the coordinates (%.2f, %.2f) and (%.2f, %.2f) is %.2f" % (x1, y1, x2, y2, m))
    return m  # output 'm' of this function is either a valid number, or a string if division by zero occurred. If string, subsequent exceptions are TypeErrors.

def yint(x_1, y_1,m):
    '''

    :param x_1: (float) with value for x1.
    :param y_1: (float) with value for y1.
    :param m: (float) with previously calculated slope, or (string) of text if ZeroDivisionError exception
               is encountered in the slope calculation.
    :return: (float) with calculated y-intercept, or (string) of text if ZeroDivisionError exception
              is encountered in the slope calculation
    '''

    try:
        b = y_1 - m*x_1
    except TypeError as e:
        print("y-int: Due to invalid division by zero, the slope is invalid, and the y-intercept cannot be calculated. Python's error message:", e)
        b = "INVALID DUE TO INVALID SLOPE: DIVISION BY ZERO"
    else:
        print("y-int: the y-intercept of the line that joins the coordinates (%.2f, %.2f) and (%.2f, %.2f) is %.2f" % (x1, y1, x2, y2, b))
    return b

def midpoint(x_1, x_2, y_1, y_2):
    '''

    :param x_1: (float) with value for x1.
    :param x_2: (float) with value for x2.
    :param y_1: (float) with value for y1.
    :param y_2: (float) with value for y2.
    :return: (tuple) containing the float values for the midpoint coordinates
    '''

    midx = (x_1 + x_2)/2
    midy = (y_1 + y_2)/2
    print("Midpoint: the midpoint of the line that joins the coordinates (%.2f, %.2f) and (%.2f, %.2f) is (%.2f, %.2f)" % (x1, y1, x2, y2, midx, midy))
    return midx, midy

# ---- Presentation (Input/Output) ---- #

# Define input/output functions here

def welcome():
    ''' Welcomes the user and gives a brief introduction as to what the program does
    
    :return: Nothing
    '''

    print("\nWelcome to the Line Geometry Program! In this program, you will be able to perform basic line geometry")
    print("calculations. With a given input for two (x,y) coordinates, the program will beb able to calculate the ")
    print("distance between the two points, the slope of the line joining the two points, the y-intercept of the ")
    print("line, and the midpoint between the two points. The results are stored in a list, which you can save to")
    print("a binary file by pickling. You can also retrieve the results by unpickling the binary file. The intention")
    print("of writing this program is to demonstrate Exception Handling and Pickling. Let's begin!")

def x1Input():
    ''' Gets user input for the first x value.

    :return: (float) with value for x1
    '''
    x1Bln = True  # used as a condition in the while loop below to exit the loop when x1Bln is still equal to True
    while True:
        x1 = input("Please enter first x coordinate x1: ").strip()
        try:
            x1 = float(x1)
        except ValueError as e: # executes if ValueError exception is encountered
            print("\nInvalid input. Coordinate x1 can only be a number. Python's error message:", e, "\n")
            x1Bln = False  # condition is False, and the while loop executes again to get valid user input for x1.
        except TypeError as e: # executes if TypeError exception is encountered
            print("\nInvalid input. Coordinate x1 can only be a number. Python's error message:", e, "\n")
            x1Bln = False  # condition is False, and the while loop executes again to get valid user input for x1.
        else:
            x1Bln = True  # if no exceptions encountered, the condition is changed to True
        if x1Bln == False:
            continue
        elif x1Bln == True:
            break
    return x1

def y1Input():
    ''' Gets user input for the first y value.

    :return: (float) with value for y1
    '''
    y1Bln = True # used as a condition in the while loop below to exit the loop when y1Bln is still equal to True
    while True:
        y1 = input("Please enter first y coordinate y1: ").strip()
        try:
            y1 = float(y1)
        except ValueError as e:  # executes if ValueError exception is encountered
            print("\nInvalid input. Coordinate y1 can only be a number. Python's error message:", e, "\n")
            y1Bln = False  # condition is False, and the while loop executes again to get valid user input for y1.
        except TypeError as e:  # executes if TypeError exception is encountered
            print("\nInvalid input. Coordinate y1 can only be a number. Python's error message:", e, "\n")
            y1Bln = False  # condition is False, and the while loop executes again to get valid user input for y1.
        else:
            y1Bln = True  # if no exceptions encountered, the condition is changed to True
        if y1Bln == False:
            continue
        elif y1Bln == True:
            break
    return y1

def x2Input():
    ''' Gets user input for the second x value.

    :return: (float) with value for x2
    '''
    x2Bln = True  # used as a condition in the while loop below to exit the loop when x2Bln is still equal to True
    while True:
        x2 = input("Please enter second x coordinate x2: ").strip()
        try:
            x2 = float(x2)
        except ValueError as e:  # executes if ValueError exception is encountered
            print("\nInvalid input. Coordinate x2 can only be a number. Python's error message:", e, "\n")
            x2Bln = False  # condition is False, and the while loop executes again to get valid user input for x2.
        except TypeError as e:  # executes if TypeError exception is encountered
            print("\nInvalid input. Coordinate x2 can only be a number. Python's error message:", e, "\n")
            x2Bln = False  # condition is False, and the while loop executes again to get valid user input for x2.
        else:
            x2Bln = True  # if no exceptions encountered, the condition is changed to True
        if x2Bln == False:
            continue
        elif x2Bln == True:
            break
    return x2

def y2Input():
    ''' Gets user input for the second y value.

    :return: (float) with value for y2
    '''
    y2Bln = True  # used as a condition in the while loop below to exit the loop when y2Bln is still equal to True
    while True:
        y2 = input("Please enter second y coordinate y2: ").strip()
        try:
            y2 = float(y2)
        except ValueError as e:  # executes if ValueError exception is encountered
            print("\nInvalid input. Coordinate y2 can only be a number. Python's error message:", e, "\n")
            y2Bln = False  # condition is False, and the while loop executes again to get valid user input for y2.
        except TypeError as e:  # executes if TypeError exception is encountered
            print("\nInvalid input. Coordinate y2 can only be a number. Python's error message:", e, "\n")
            y2Bln = False  # condition is False, and the while loop executes again to get valid user input for y2.
        else:
            y2Bln = True  # if no exceptions encountered, the condition is changed to True
        if y2Bln == False:
            continue
        elif y2Bln == True:
            break
    return y2

def output_menu_tasks():
    ''' Outputs the menu tasks each time a menu task is completed, so that the user can easily see what tasks
        can be performed next.

    :return: Nothing
    '''

    print('''
    Menu of Options
    1) Perform Line Geometry Calculations
    2) Pickle Data to Binary File
    3) Unpickle Data from Binary File 
    4) Exit Program
    ''')
    pass

def input_menu_choice():
    ''' Gets user input for menu choice selection

    :return: (string) containing the user's selected menu choice.
    '''
    choice = str(input("Select a menu option: ").strip())  # if a valid menu choice is not selected, the user sees the menu again.
    return choice


# ---- Main Body of Script ---- #
welcome()

while True:
    output_menu_tasks()
    strChoice = input_menu_choice()

    if strChoice == "1":
        counter = counter + 1  # counter is used to count how many times the program has been run for calculations
    # Get user input: coordinates
        print("1) Perform Line Geometry Calculations\n")
        x1 = x1Input()
        y1 = y1Input()
        mathDict["(x1,y1)"] = (x1,y1) # becomes a tuple that is stored into the dictionary
        x2 = x2Input()
        y2 = y2Input()
        mathDict["(x2,y2)"] = (x2,y2)

    # Calculate values:
        d = distance(x1,x2,y1,y2)
        mathDict["Distance"] = "%.2f" % d

        m = slope(x1,x2,y1,y2)  # possibility of TypeError here due to the way the ZeroDivisionError exception was handled in the slope function.
        try:  #handling potential TypeError
            mathDict["Slope"] = "%.2f" % m
        except TypeError:
            mathDict["Slope"] = "Invalid slope due to division by zero."

        b = yint(x1,y1,m)   # possibility of TypeError here due to the way the ZeroDivisionError exception was handled in the slope function.
        try:  #handling potential TypeError
            mathDict["y-int"] = "%.2f" % b
        except TypeError:
            mathDict["y-int"] = "Invalid y-intercept due to invalid slope: division by zero"

        midx, midy = midpoint(x1,x2,y1,y2)
        mathDict["Midpoint"] = "(%.2f, %.2f)" % (midx, midy)

        mathDictVar = mathDict.copy()  # by making a copy of the dictionary, a new reference to the dictionary is created,
                                       # so previous dictionary values in the list are not overwritten (as dictionary values are mutable)
        mathDictList.append(mathDictVar)

        print("\nThe current list of calculations is: \n", mathDictList)  # to see if the program is working. Will remove later so user does not see every time
        print("\nThe values above have been stored locally in a List as a Dictionary object. ")
        continue

    elif strChoice == "2":
        print("2) Pickle Data to Binary File \n")
        binFile = open("geomCalcs.dat","wb")  # open the binary file, specifying that data is to be overwritten each
                                              # time program is run, to only keep contents of current session.
        for row in mathDictList:
            pickle.dump(row, binFile)  # use the pickle.dump() function for each row in the list, so that each dictionary
                                       # can be saved in a separate line of the file.
        binFile.close()
        print("Data successfully pickled. ")
        continue

    elif strChoice == "3":
        print("3) Unpickle Data from Binary File \n")
        binFile = open("geomCalcs.dat","rb")   # open the binary file, specifying the "read" access mode
        while i <= counter:  # pickle.load() unpickles one line at a time, so only run through the loop if 'i' is less
                             # than the number of times the program was run
            try:
                unpickled = pickle.load(binFile)
                print("Calculation #", i+1, ":", unpickled)  # clearly display each calculation to user
                i = i+1
            except EOFError:  # If pickle.load() runs out of input by reaching the end of the file, which is represented
                              # by the EOFError exception, break the while loop
                break
        binFile.close()
        continue

    elif strChoice == "4":
        print("Program terminating... ")
        break