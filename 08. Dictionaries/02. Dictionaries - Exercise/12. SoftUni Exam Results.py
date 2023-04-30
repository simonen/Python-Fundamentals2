command = input()

submissions = {}
book = {}
while command != "exam finished":
    command = command.split("-")
    if command[1] == 'banned':
        student = command[0]
        del(book[student])
        command = input()
        continue

    student, language, score = command[0], command[1], int(command[2])
    if student not in book:
        book[student] = 0
    if score > book[student]:
        book[student] = score
    if language not in submissions:
        submissions[language] = 0
    submissions[language] += 1

    command = input()

print("Results:")
for student, score in book.items():
    print(f"{student} | {score}")
print('Submissions:')
for k, v in submissions.items():
    print(f"{k} - {v}")
