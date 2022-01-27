import math


# Stuff to be renamed
equals =       "EMANCIPATION PROCLAMATION"
add =          "WW2"
subtract =     "GHENGIS KHAN"
multiply =     "SHREK"
divide =       "JFK"
exponent =     "THE GENOVA CONVENTION"
squareRoot =   "GANGNAM STYLE"
Print =        "CRUSADES"



# Get code from file
with open("pythagorean.hist") as file:
	esolangInput = file.read()

esolangInput = esolangInput.replace(equals, "=")
esolangInput = esolangInput.replace(add, "+")
esolangInput = esolangInput.replace(subtract, "-")
esolangInput = esolangInput.replace(multiply, "*")
esolangInput = esolangInput.replace(divide, "/")
esolangInput = esolangInput.replace(exponent, "**")
esolangInput = esolangInput.replace(squareRoot, "math.sqrt")
esolangInput = esolangInput.replace(Print, "print")

exec(esolangInput)