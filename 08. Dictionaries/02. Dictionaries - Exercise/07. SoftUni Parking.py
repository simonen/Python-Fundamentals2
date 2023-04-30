n = int(input())

parking = {}

for i in range(n):
    command = input().split()
    action, username = command[0], command[1]
    if action == "register":
        license_plate = command[2]
        if username not in parking:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif action == "unregister":
        if username in parking:
            del(parking[username])
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")


for user, plate in parking.items():
    print(f"{user} => {plate}")
