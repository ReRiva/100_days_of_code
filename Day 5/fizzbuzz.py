# Replicating the fizz buzz game

target = 100

for number in range(1, target + 1):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0 :
        print("Buzz")
    else:
        print(number)