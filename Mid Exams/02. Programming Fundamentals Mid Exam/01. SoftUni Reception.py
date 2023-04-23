employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students = int(input())

hours = 0
while students > 0:
    hours += 1
    if hours % 4 == 0:
        hours += 1
    students -= (employee1 + employee2 + employee3)

print(f"Time needed: {hours}h.")