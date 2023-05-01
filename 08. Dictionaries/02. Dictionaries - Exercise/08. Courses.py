command = input()
database = {}

while command != "end":
    course, student = command = command.split(" : ")
    if course not in database:
        database[course] = []
    database[course].append(student)

    command = input()

for course, students in database.items():
    print(f"{course}: {len(students)}")
    joined = "\n-- ".join(students)
    print(f"-- {joined}")
