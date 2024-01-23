
# Program to decide who is going to pay the bill
import random

# List of names

names = ["Carlos", "Pedro", "Maria", "John", "Karl", "Martha", "Samantha"]


person_paying = random.randint(0, (len(names))-1)

print(f"The Peson paying the bill todays is {names[person_paying]}. Congratulations haha")