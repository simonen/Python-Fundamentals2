encrypted_msg = list(input())
command = input()

while command != "Decode":
    command = command.split("|")
    action = command[0]
    if action == "Move":
        first_letters = int(command[1])
        encrypted_msg = encrypted_msg[first_letters:] + encrypted_msg[:first_letters]
    elif action == "Insert":
        index = int(command[1])
        string = command[2]
        encrypted_msg.insert(index, string)
        encrypted_msg = list("".join(encrypted_msg))

    elif action == "ChangeAll":
        subs1 = command[1]
        subs2 = command[2]
        if subs1 in "".join(encrypted_msg):
            encrypted_msg = list("".join(encrypted_msg).replace(subs1, subs2))

    command = input()

print(f"The decrypted message is: {''.join(encrypted_msg)}")
