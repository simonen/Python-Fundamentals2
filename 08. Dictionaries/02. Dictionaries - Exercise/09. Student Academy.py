rows = int(input())

book = {}
for row in range(rows):
    student = input()
    grade = float(input())
    if student not in book:
        book[student] = []
    book[student].append(grade)

for student, grades in book.items():
    average = sum(grades) / len(grades)
    if average >= 4.5:
        print(f"{student} -> {average:.2f}")
