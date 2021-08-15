#two dices
#importing module for random number generation
import random
option_1 = [1,2]

choice = int(input("How many dices do you wish to simulate(1 or 2)?: "))
while choice in option_1:
    if choice==2:
        #range of the values of a dice
        min_val = 1
        max_val = 6

        #to loop the rolling through user input
        roll_again = "yes"

        #loop
        while roll_again == "yes" or roll_again == "y":
            print("Rolling The Dices...")
            print("The Values are :")
    
            #generating and printing 1st random integer from 1 to 6
            print(random.randint(min_val, max_val))
    
            #generating and printing 2nd random integer from 1 to 6
            print(random.randint(min_val, max_val))
    
            #asking user to roll the dice again. Any input other than yes or y will terminate the loop
            roll_again = input("Roll the Dices Again (yes/y or no/n)?") 
    
    if choice==1:
        # Importing randome module
        # Initiating an while loop to keep the program executing
        while True:
            print("Rolling Dice...")

            # Using random.randint(1,6) to generate a random value between 1 & 6
            print(f"The value is ", random.randint(1,6))

            # Asking user to roll the dice again or quit 
            repeat = input("Roll Dice again? 'y' for yes & 'n' for no: ")

            # If the user answers negative the loop will break and program execution stops otherwise the program will continue executing 
            if repeat == 'n':
                break
    choice = int(input("How many dices do you wish to simulate(1 or 2) (enter a random number other than 1 or 2 to terminate the program) ?: "))
