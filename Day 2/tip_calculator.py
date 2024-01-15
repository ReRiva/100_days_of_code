# Tip calculator

print("Welcome to the tip calculator\n")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? "))
total_people = int(input("How many people are splitting the bill? "))

bill_per_person = round((total_bill * (1 + tip_percentage/100)) / total_people, 2)

print(f"Each person should pay: ${bill_per_person}")