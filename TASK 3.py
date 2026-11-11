
number_of_grades = int(input("How many grades? "))

total = 0

for i in range(number_of_grades):
    grade = float(input("Enter grade: "))
    total += grade

average = total / number_of_grades

print("Average:", format(average, ".2f"))

if average >= 3.0:
    print("Student passed.")
else:
    print("Student failed.")
