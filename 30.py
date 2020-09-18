kilopa = float(input("Pressure in kilopascal: "))

ppsi = kilopa/6.89475729
milimerc = kilopa *760 /101.325
atm = kilopa/101.325

print("Pressure  in pounds per square inch:%.2f psi"%ppsi)
print("Pressure in milimetr of mercury:%.2f psi"%milimerc)
print("Atmosphere presssure:%.2f atm"%atm)
