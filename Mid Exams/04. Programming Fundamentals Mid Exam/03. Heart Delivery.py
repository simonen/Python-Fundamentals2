houses = list(map(int, input().split("@")))
command = input()

index = 0
while command != 'Love!':
    command = command.split()
    jump = int(command[1])
    index += jump
    if index > len(houses) - 1:
        index = 0
    houses[index] -= 2
    if houses[index] == 0:
        print(f"Place {index} has Valentine's day.")
    elif houses[index] < 0:
        print(f"Place {index} already had Valentine's day.")
        houses[index] = 0

    command = input()

print(f"Cupid's last position was {index}.")
failed_houses = len(houses) - houses.count(0)
if failed_houses <= 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_houses} places.")
