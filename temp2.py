# create a code that converts celcius to fahrenheit
# the formula for celcius to fahrenheit is degree(celcius) * (9/5) + 32
# create a function to run this code

def celcius_to_fahranheit(celcius):
    """This function takes an argument (celcius) and converts that number
    to a fahrenheit degree from celcius degrees"""
    # formula for celcius to fahranheit is degree(celcius) * (9/5) + 32
    return celcius * (9/5) + 32

celcius = 25    
conversion = celcius_to_fahranheit(celcius)
print(f"{celcius} degrees celcius is {conversion} degrees fahrenheit")