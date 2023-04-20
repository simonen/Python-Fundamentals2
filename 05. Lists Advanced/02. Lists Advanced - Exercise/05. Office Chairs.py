rooms = int(input())

free_chairs = 0
are_rooms_supplied = True

for room in range(1, rooms + 1):
    command = input().split()
    chairs = len(command[0])
    visitors = int(command[1])
    if chairs < visitors:
        print(f"{abs(chairs - visitors)} more chairs needed in room {room}")
        are_rooms_supplied = False
    else:
        free_chairs += chairs - visitors

if are_rooms_supplied is True:
    print(f"Game On, {free_chairs} free chairs left")
