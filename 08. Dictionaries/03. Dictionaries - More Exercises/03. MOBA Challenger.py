book = {}
command = input()

while command != "Season end":
    action = command.split()
    if action[1] == 'vs':
        player1, player2 = action[0], action[2]
        checks = (
            (player1 in book and player2 in book) and
            any(x in book[player1].keys() for x in book[player2].keys())
        )
        if checks:
            player1_pts = sum(book[player1].values())
            player2_pts = sum(book[player2].values())
            if player1_pts > player2_pts:
                del (book[player2])
            elif player1_pts < player2_pts:
                del(book[player1])
        command = input()
        continue

    player, position, skill = command.split(" -> ")
    if player not in book:
        book[player] = {}
    if position not in book[player] or book[player][position] < int(skill):
        book[player][position] = int(skill)

    command = input()

for user, positions in sorted(book.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{user}: {sum(positions.values())} skill")
    for position, skill in sorted(positions.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
