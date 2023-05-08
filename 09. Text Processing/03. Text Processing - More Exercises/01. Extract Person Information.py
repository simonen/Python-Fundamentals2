n = int(input())

for _ in range(n):
    string = input().split()
    name = ''
    age = 0
    for i in string:
        if '@' in i and '|' in i:
            index1 = i.index("@")
            index2 = i.index("|")
            name = i[index1 + 1:index2]
        if "#" in i and "*" in i:
            index1 = i.index("#")
            index2 = i.index("*")
            age = i[index1 + 1:index2]
    print(f"{name} is {age} years old.")
