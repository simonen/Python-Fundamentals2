command = input()

contests = {}
while command != 'end of contests':
    contest, password = command.split(':')
    contests[contest] = password

    command = input()

command = input()
submissions = {}
while command != 'end of submissions':
    contest, password, username, points = command.split('=>')
    if contest not in contests or contests[contest] != password:
        command = input()
        continue
    if username not in submissions:
        submissions[username] = {}
    if contest not in submissions[username] or submissions[username][contest] < int(points):
        submissions[username][contest] = int(points)

    command = input()

winner = sorted(submissions.items(), key=lambda x: -sum(x[1].values()))[0][0]
max_points = sum(submissions[winner].values())

print(f"Best candidate is {winner} with total {max_points} points.\nRanking:")

for user, contests in sorted(submissions.items(), key=lambda x: x[0]):
    print(user)
    for contest, score in sorted(contests.items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {score}")

# winner = ''
# max_points = 0
# for username, contest in submissions.items():
#     if sum(contest.values()) > max_points:
#         max_points = sum(contest.values())
#         winner = username