temperature = float(input("Air temperaure in Celcius: "))
speed = float(input("The wind speed: " ))

wind_chill_index = 13.12 + (0.6215*temperature) + (-11.37*speed*0.16) + (0.3965*temperature*speed**0.16)
print("Wind chill index: %.2f" % wind_chill_index)