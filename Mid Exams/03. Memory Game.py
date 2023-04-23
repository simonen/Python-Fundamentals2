seq = input().split()
command = input()

turns = 0
while command != 'end':
    turns += 1
    command = command.split()
    ind1, ind2 = int(command[0]), int(command[1])
    if ind1 == ind2 or (ind1 not in range(len(seq)) or ind2 not in range(len(seq))):
        seq.insert(len(seq) // 2, f"-{turns}a")
        seq.insert(len(seq) // 2, f"-{turns}a")
        print("Invalid input! Adding additional elements to the board")
    elif seq[ind1] != seq[ind2]:
        print("Try again!")
    elif seq[ind1] == seq[ind2]:
        print(f"Congrats! You have found matching elements - {seq[ind1]}!")
        seq[ind1] = 'X'
        seq[ind2] = 'X'
        for _ in range(seq.count(seq[ind1])):
            seq.remove("X")
    if not any(seq.count(x) > 1 for x in seq):
        print(f"You have won in {turns} turns!")
        break

    command = input()

else:
    print("Sorry you lose :(")
    print(" ".join(seq))
