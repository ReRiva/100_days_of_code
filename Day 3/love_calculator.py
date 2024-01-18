# Using a "TOTALLY ACCURATE" method to compare two person name to compare their love compatibility

# It counts how namy times the letters T.R.U.E appear and add the count together. Then it count how many times
# the letters L.O.V.E appear add the count together and then create a two digit number with the total of counts 
# of True + Love

name1 = input("what's your name? ")
name2= input("what's their name? ")

# Combining both names in one string
combined_names = name1 + name2

# Converting string to lower case
lower_names = combined_names.lower()
print(lower_names)

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e

# Converting to str to combine both digits together(instead of adding them) and after that converting back
# to int as it will be used to compare it to another number.

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos. ")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together ")
else:
    print(f"Your score is {score}. ")