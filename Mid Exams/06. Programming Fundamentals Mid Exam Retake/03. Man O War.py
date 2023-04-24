pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
health_cap = int(input())
command = input()

while command != 'Retire':
    command = command.split()
    action = command[0]
    if action == "Fire" and int(command[1]) in range(len(warship)):
        index = int(command[1])
        damage = int(command[2])
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            break
    elif action == "Defend" and int(command[1]) in range(len(pirate_ship)) and int(command[2]) in range(len(pirate_ship)):
        start_ind = int(command[1])
        end_ind = int(command[2])
        damage = int(command[3])
        for i in range(start_ind, end_ind + 1):
            pirate_ship[i] -= damage
        if any(x <= 0 for x in pirate_ship):
            print("You lost! The pirate ship has sunken.")
            break
    elif action == "Repair" and int(command[1]) in range(len(pirate_ship)):
        index = int(command[1])
        repair = int(command[2])
        if pirate_ship[index] + repair > health_cap:
            repair = health_cap - pirate_ship[index]
        pirate_ship[index] += repair
    elif action == "Status":
        count = [x for x in pirate_ship if x < health_cap * 0.2]
        print(f"{len(count)} sections need repair.")

    command = input()

else:
    print(f"Pirate ship status: {sum(pirate_ship)}\n"
          f"Warship status: {sum(warship)}")
