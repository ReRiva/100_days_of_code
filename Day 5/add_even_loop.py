# Adding only the even numbers from a range of numbers

target = int(input("Please enter a number: "))

total_even = 0

for number in range(0, target+1):
    if number % 2 == 0:
        total_even += number

print(total_even)