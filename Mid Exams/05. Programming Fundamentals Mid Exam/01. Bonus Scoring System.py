from math import ceil

students = int(input())
lectures = int(input())
add_bonus = int(input())

max_attendances = 0
max_bonus = 0
for student in range(students):
    attendance = int(input())
    if attendance > max_attendances:
        max_attendances = attendance
    max_bonus = max_attendances / lectures * (5 + add_bonus)

print(f"Max Bonus: {ceil(max_bonus)}.\n"
      f"The student has attended {max_attendances} lectures.")
