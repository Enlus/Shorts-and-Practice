inches_str = input("What is the inches?")
inches_float = float(inches_str)
volume = (inches_float*1/12)*43560 #Because a feet is 12 inches, and 43560 is in feet we are dividing it by 12 to have the same converasion.
print(volume)
gallons = 7.48052*volume
print(gallons)
