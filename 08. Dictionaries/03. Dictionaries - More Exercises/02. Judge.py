command = input()

courses = {}
submissions = {}
while command != 'no more time':
    username, contest, points = command.split(" -> ")
    if username not in submissions:
        submissions[username] = {}
    if contest not in courses:
        courses[contest] = 0
    if contest not in submissions[username]:
        courses[contest] += 1
    if contest not in submissions[username] or submissions[username][contest] < int(points):
        submissions[username][contest] = int(points)

    command = input()

for contest, participants in courses.items():
    number = 1
    print(f"{contest}: {participants} participants")
    filtered = {x: v for x, v in submissions.items() if contest in v}
    for user, contests in sorted(filtered.items(), key=lambda x: (-x[1][contest], x[0])):
        if contest in contests:
            print(f"{number}. {user} <::> {contests[contest]}")
            number += 1

print('Individual standings:')
number = 1

for user, contest in sorted(submissions.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{number}. {user} -> {sum(contest.values())}")
    number += 1
