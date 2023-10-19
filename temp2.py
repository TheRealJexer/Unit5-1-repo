# create a code that converts celcius to fahrenheit
# the formula for celcius to fahrenheit is degree(celcius) * (9/5) + 32
# create a function to run this code

def celcius_to_fahranheit(n):
    """This function takes an argument (n) and converts that number
    to a fahrenheit degree from a (n) celcius degree"""
    # formula for celcius to fahranheit is degree(celcius) * (9/5) + 32
    return n * (9/5) + 32
    
conversion = celcius_to_fahranheit(25)
print(f"25 degrees celcius is {conversion} degrees fahranheit")