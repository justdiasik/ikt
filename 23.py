from math import tan,pi
length  = float(input())
number  = float(input())
area=(number*length**2)/(4*tan(pi/number))
print(area)