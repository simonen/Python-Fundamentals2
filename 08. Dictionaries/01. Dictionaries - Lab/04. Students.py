command = input()
students = {}

while len(command.split(":")) == 3:
    command = command.split(":")
    student, s_id, course = command[0], int(command[1]), command[2]
    students[student] = {}
    students[student]["ID"] = s_id
    students[student]["Course"] = course
    command = input()

for student, v in students.items():
    s_id = v['ID']
    course = v['Course']
    if command == course.replace(" ", "_"):
        print(f"{student} - {s_id}")
