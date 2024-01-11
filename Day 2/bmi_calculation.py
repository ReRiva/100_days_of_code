# BMI Calculation Program - 100 days of code Day 2

height = float(input("Please enter your height in meters. "))
weight = float(input("Please enter your weight in kilograms. "))

bmi =  weight / (height**2)

# Printing BMI as integer as requested
print(int(bmi))