mass = float(input("Water in mm "))
temperature = float(input("Temperature Celsius "))

heat_capacity_water = 4.186
electricity_cost = 8.9 
j_kwh = 2.777**-7

Q = heat_capacity_water*mass*temperature
print("%d. joules of energy "%Q)

kilowatt_hours = Q * j_kwh
cost = electricity_cost * kilowatt_hours

print("This energy costs %.2f cents"%cost)