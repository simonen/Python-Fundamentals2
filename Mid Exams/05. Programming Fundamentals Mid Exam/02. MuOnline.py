health, bitcoin = 100, 0
dungeon = input().split("|")

for i in range(0, len(dungeon)):
    command = dungeon[i].split()[0]
    number = int(dungeon[i].split()[1])
    if command == "potion":
        if health + number > 100:
            number = 100 - health
        health += number
        print(f"You healed for {number} hp.\n"
              f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        bitcoin += number
    else:
        monster = command
        health -= number
        if health <= 0:
            print(f"You died! Killed by {monster}.\n"
                  f"Best room: {i + 1}")
            break
        print(f"You slayed {monster}.")
else:
    print(f"You've made it!\n"
          f"Bitcoins: {bitcoin}\n"
          f"Health: {health}")
