
#################################################
# Name: Alex Katrompas
# Assignment: Demo Functions
# Purpose of the file: Demonstration code for
# learning and understanding functions.
#################################################

import functions as fn
#from functions import fibonacci # this is an alternate form

# defines main, does not run it
def main():
    """
    This is the driver function. It has no parameters.
    Ask the user for a positive int, calculate the
    Fibonacci series by calling fibonacci and display
    the result. 

    @param na : na

    @return na : na

    @exception na : na

    @note Driver functions stand alone in driver files!
    """
    
#    print(fibonacci.__doc__)
#    exit()

    number = input("Enter a positive integer: ")
    try:
        number = int(number)
    except:
        number = 0

    if number > 0:
        fib = fn.fibonacci(number) # function call, number is the argument
        print("The fibinacci result of",number,"is", fib)
    else:
        print("Error: Enter a positive integer")

# calls main, starts the program
# this is the driver function
main()

