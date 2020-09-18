r = 8.314
p = int(input("Enter the pressure in the pascals"))
v = int(input("Enter the volume in litres"))
t = int(input("Enter the temperature in degrees kelvin"))
n = (p*v) / (r*t)
print("The amount of substance in moles is:", n)