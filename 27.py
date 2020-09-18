height = float(input("Your height in inches: "))
weight = float(input("Your weight in pounds: "))

BMI = weight/(height*height)*703
print("Its your body mass index: %.2f" % BMI)

height = float(input("Your height in meters: "))
weight = float(input("Your weight in kilogram: "))

BMI = weight/(height*height)
print("Its your body mass index: %.2f" % BMI)