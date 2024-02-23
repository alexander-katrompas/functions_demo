
#################################################
# Name: Alex Katrompas
# Assignment: Demo Functions
# Purpose of the file: Demonstration code for
# learning and understanding functions.
#################################################


# defines fibonacci, does not run it
def fibonacci(n): # this is a function header, n is a parameter, i.e. input
    """ this is a doc string

    This function accepts one positive value,
    calculates the end result of the fibonacci
    series of that number, and returns it.

    @param (int) n : fibbonacci number

    @return (int) answer : fibbonacci result

    @exception na : na

    @note this function only returns the result, not the series
    """
        
    answer = None #start with a default return that says, "didn't process yet"
    if type(n) == type(1) and n > 0: #validation
        n1, n2 = 0, 1
        for _ in range(n): #processing
            n1, n2 = n2, n1 + n2
        answer = n1
    return answer #return, i.e. "output"


