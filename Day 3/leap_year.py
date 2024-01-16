# Program to check if a Year is a leap year or not

year = int(input("Please enter a Year. "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is a not leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")