from math import radians , sin , cos , asin , sqrt
latitude1 = float(input("enter latitude 1: "))
latitude2 = float(input("enter latitude 2: "))
longitude1 = float(input("enter longitude 1: "))
longitude2 = float(input("enter longitude 2: "))

longitude1 = radians(longitude1)
longitude2 = radians(longitude2)
latitude1 = radians(latitude1)
latitude2 = radians(latitude2)

latd = latitude2 - latitude1
lond = longitude2 - longitude1

k = sin(latd/2)**2 + cos(latitude1) * cos(latitude2) * sin(lond/2)**2
r = 6371
l = 2 * asin(sqrt(k))

print("distance between the points:",l*r,"km")
