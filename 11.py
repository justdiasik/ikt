liter_to_gallon = 3.785411784
km_to_miles = 1.609344

def c_mileage(miles_to_gallon):
    return (100*liter_to_gallon)/(km_to_miles*miles_to_gallon)
def need_l(distance_km,miles_to_gallon):
    liter_to_100km = c_mileage(miles_to_gallon)
    return liter_to_100km *  distance_km /100
print("Liters need for 200 km with 15mpg:",need_l(354,18))
