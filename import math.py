import re

def getUserFunction(): # still doesn't work for trig fonctions, will have to look into that
    

    function_str = input("Enter a elementary function in python syntax: ")
    
    # Regular expressions was something I learned while doing this
    pattern = r'^[0-9+\-*/().\s^x]+(?:sin|cos|tan|sqrt|log|exp)*[0-9+\-*/().\s^x]+$'
    
    if not re.match(pattern, function_str):
        print("Invalid input. Please enter a valid mathematical expression.")
        return None
    
    try:
        # Using an eval method to see if the input works
        def userfunction(x):
            return eval(function_str)
        
        return userfunction
    
    except Exception as error:
        print("Error:", error , "try again")
        return None



def elevenPointNewtonCotesFormula(y, a, b):
    deltaX = (b-a)/1000
    ## I took the math from shauns notes on numerial analysis
    returnValue =0
    for l in range(1001):
        if (l ==0 or l==1000):
            returnValue += 16067*y(a+l*deltaX)
        elif (l%10==1 or l%10==9):
            returnValue += 106300*y(a+l*deltaX)
        elif (l%10 ==2 or l%10==8):
            returnValue -= 48525*y(a+l*deltaX)
        elif (l%10==3 or l%10==7):
            returnValue += 272400*y(a+l*deltaX)
        elif(l%10==4 or l%10==6):
            returnValue -= 260550*y(a+l*deltaX) 
        elif(l%10==5):
            returnValue += 427368*y(a+l*deltaX)
        else:
            returnValue += 32134*y(a+l*deltaX)    
    returnValue *= 5*deltaX/299376
    return returnValue 


    
        
userfunction = getUserFunction()
while True:
    try:
        firstValue = int(input("Start of interval: "))
        secondValue = int(input("End of interval: "))
        break  # If conversion is successful, exit the loop
    except ValueError:
        print("Please enter valid integers for the interval.")
print( '%.5f' % elevenPointNewtonCotesFormula(userfunction, firstValue, secondValue))





