# BMI Calculation Program - 100 days of code Day 3

height = float(input("Please enter your height in meters. "))
weight = float(input("Please enter your weight in kilograms. "))

bmi = round(weight / (height**2), 1)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:    
    print(f"Your BMI is {bmi}, you are clinically obese.")