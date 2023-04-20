def exercise(lesson_f, lessons_f):
    if lesson_f not in lessons:
        lessons_f.append(lesson_f)
    index1 = lessons.index(lesson_f)
    if lesson_f + '-Exercise' not in lessons_f:
        lessons_f.insert(index1 + 1, lesson_f + '-Exercise')
    return lessons_f


def remove(lesson_f, lessons_f):
    if lesson_f + "-Exercise" in lessons_f:
        lessons_f.remove(lesson_f + "-Exercise")
    lessons_f.remove(lesson_f)
    return lessons_f


def swap(lesson1_f, lesson2_f, lessons_f):
    index1 = lessons_f.index(lesson1_f)
    index2 = lessons_f.index(lesson2_f)
    lessons_f[index1], lessons_f[index2] = lessons_f[index2], lessons_f[index1]
    if lesson1_f + '-Exercise' in lessons_f:
        exercise1 = lessons_f.pop(lessons_f.index(lesson1_f + '-Exercise'))
        lessons_f.insert(lessons_f.index(lesson1_f) + 1, exercise1)
    if lesson2_f + '-Exercise' in lessons_f:
        exercise2 = lessons_f.pop(lessons_f.index(lesson2_f + '-Exercise'))
        lessons_f.insert(lessons_f.index(lesson2_f) + 1, exercise2)
    return lessons_f


lessons = input().split(", ")
command = input()

while command != 'course start':
    command = command.split(":")
    action = command[0]
    lesson = command[1]
    if action == 'Add' and lesson not in lessons:
        lessons.append(lesson)
    elif action == "Insert" and lesson not in lessons:
        index = int(command[2])
        if index <= len(lessons) - 1:
            lessons.insert(index, lesson)
        if "-Exercise" in lessons[index + 1]:
            lessons[index], lessons[index + 1] = lessons[index + 1], lessons[index]
    elif action == "Remove" and lesson in lessons:
        lessons = remove(lesson, lessons)
    elif action == "Swap" and lesson in lessons and command[2] in lessons:
        lessons = swap(lesson, command[2], lessons)
    elif action == "Exercise":
        lessons = exercise(lesson, lessons)
    # print(lessons)
    command = input()

for i in range(0, len(lessons)):
    print(f"{i + 1}.{lessons[i]}")