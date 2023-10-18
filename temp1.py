# create a code that converts celcius to fahrenheit
# the formula for celcius to fahrenheit is degree(celcius) * (9/5) + 32
celcius = 25

def celcius_to_fahrenheit(celcius):
    conversion_formula = celcius * (9/5) + 32
    print(f"25 degress celcius is {int(conversion_formula)} degrees fahrenheit.")
    return celcius

fahrenheit = celcius_to_fahrenheit(celcius)



