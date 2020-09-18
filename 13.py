per_nickels = 5
per_dimes = 10
per_quarters = 25 
per_loonies = 100
per_toonies = 200

cost = int(input("Your cost is: "))
print( cost//per_nickels,"nickels" )
cost = cost%per_nickels
print(cost, "pennies")

cost = int(input("Your cost is: "))
print( cost//per_dimes,"dimes" )
cost = cost%per_dimes
print(cost, "pennies")

cost = int(input("Your cost is: "))
print( cost//per_quarters,"quarters" )
cost = cost%per_quarters
print(cost, "pennies")

cost = int(input("Your cost is: "))
print( cost//per_loonies,"loonies" )
cost = cost%per_loonies
print(cost, "pennies")

cost = int(input("Your cost is: "))
print( cost//per_toonies,"toonies" )
cost = cost%per_toonies
print(cost, "pennies")