# Calculating how many weeks a person has left(based on their age) if we assume that said person will live until 90 years old

# A year has around 52 weeks
weeks_year = 52
# 90 years has a total of 4.500 weeks
total_weeks = 52 * 90

# Asking for a user age
age = int(input("Please enter your age. "))

# Calculating how many weeks the user has left
weeks_left = total_weeks - (age * weeks_year)

print(f"You have {weeks_left} weeks left\n")