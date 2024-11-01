'''
Author: Samuel Ragsdale
Date: 11/01/2024
Name: sragsdale_gpacheck_sdev220.py
Description: This is a simple python program that takes as inputs the student's last name,
first name & GPA. It then prints out various congratulation messages if the GPA falls within
certain ranges. Finally the process is a restartable loop that can be triggered or abandoned
by user inputs after the initial information is collected.
'''

'''Initialized variables for the student's first, last name & GPD'''
studentLast = ""
studentFirst = ""
studentGPA = 0.0

'''while loop that will accept last names, first names & GPA scores. Will print messages if the GPA is 3.5 or greater (Dean's List), 
or 3.25 or greater (Honor Roll). It will also ask if the user wants to restart the loop at the end, just for ease of testing.'''
while True:
    studentLast = input("Enter the student's last name: ")
    if studentLast == "ZZZ":
        break
    studentFirst = input("Enter the student's first name: ")
    studentGPA = float(input("Enter the student's GPA: "))

    if studentGPA >= 3.5:
        '''f string which prints the concatenated username & that they've made the Dean's list if GPA is greater than or equal to 3.5'''
        print(f"Congratulations, {studentFirst} {studentLast} has made the Dean's List!")
        pass
    elif studentGPA >= 3.25 and studentGPA < 3.5:
        '''f string which prints concatenated username & that they've made the honor roll if GPA falls between 3.25 and 3.5'''
        print(f"Congratulations, {studentFirst} {studentLast} has made the Honor Roll!")
        pass
    
    restartChoice = input("Do you want to enter another student? (y/n)")
    '''restartChoice will trigger a break in the loop if the user doesn't enter y'''
    if restartChoice != "y":
        print("Thank you, have a good day.")
        break

