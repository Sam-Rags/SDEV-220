'''
Author: Samuel Ragsdale
Date written: October 29, 2024
Description: 6.1 Use a for loop to print the values of the list [3, 2, 1, 0].

6.2 Assign the value 7 to the variable guess_me, and the value 1 to the variable number. 
Write a while loop that compares number with guess_me. Print 'too low' if number is less than guess me. 
If number equals guess_me, print 'found it!' and then exit the loop. If number is greater than guess_me, print 'oops' and then exit the loop. 
Increment number at the end of the loop.

6.3 Assign the value 5 to the variable guess_me. 
Use a for loop to iterate a variable called number over range(10). 
If number is less than guess_me, print 'too low'. If it equals guess_me, print found it! and then break out of the for loop. 
If number is greater than guess_me, print 'oops' and then exit the loop.
'''
#6.1 below
list = [3, 2, 1, 0]

for n in list:
    print(n)
    

#6.2 below
guess_me = 7
number = 1

while number <= guess_me:
    if number < guess_me:
        print("too low")
        number += 1
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break


#6.3 below
guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops!")
        break