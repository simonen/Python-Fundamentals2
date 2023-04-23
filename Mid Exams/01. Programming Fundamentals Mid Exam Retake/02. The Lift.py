people = int(input())
lift = list(map(int, input().split()))

people_left = people + sum(lift) - len(lift) * 4
if people_left < 0:
    print("The lift has empty spots!")
if people_left > 0:
    lift = [4] * len(lift)
    print(f"There isn't enough space! {people_left} people in a queue!")
else:
    for i in range(len(lift)):
        seats = 4 - lift[i]
        if people >= seats:
            people -= seats
            lift[i] += seats
        else:
            lift[i] += people
            people = 0

print(" ".join(list(map(str, lift))))
