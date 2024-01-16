
# if/else statements

height = int(input("What's your height in cm? "))
bill = 0

# Checking customer age and height to determine the price of the ticket and if they can ride.

if height >= 120:
    print("You can ride the rollercoaster ")
    age = int(input("What's your age? "))
    if age > 18:
        bill = 12
        print("Adult tickets are $12.")
    elif age < 12:
        bill = 5
        print("Child tickets are $5.")
    else:
        bill = 7
        print("Youth tickets are $7.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Total of your ticket is {bill}.")
  

else:
    print("Sorry, you have to grow taller before you can ride. ")