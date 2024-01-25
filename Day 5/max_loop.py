# Find the max score using for loops


students_score = [78,65,89,86,55,91,64,89]
i = 0
max_score = students_score[0]
for score in students_score:
    if students_score[i] > max_score:
        max_score = score
    i += 1
print(f"The highest score in the class is: {max_score}.")
