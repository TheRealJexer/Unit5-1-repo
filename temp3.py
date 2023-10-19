# create a code that converts celcius to fahrenheit
# the formula for celcius to fahrenheit is degree(celcius) * (9/5) + 32
# the formula for fahrenheit to celcius is [(degree(fahrenheit) - 32) * 5] / 9 
celcius = 25
fahrenheit = 82

def celcius_to_fahrenheit(celcius):
    """This function converts the argument (celcius) degrees to fahrenheit"""
    conversion_formula = celcius * (9/5) + 32
    return print(f"{celcius} degress celcius is {int(conversion_formula)} degrees fahrenheit")

def fahrenheit_to_celcius(fahrenheit):
    """This function converts the argument (fahrenhiet) degress to celcius"""
    conversion_formula1 = ((fahrenheit - 32) * 5) / 9
    return print(f"{fahrenheit} degress fahrenheit is {int(conversion_formula1)} degrees celcius")

temp_fahrenheit = celcius_to_fahrenheit(celcius)
temp_celcius = fahrenheit_to_celcius(fahrenheit)



