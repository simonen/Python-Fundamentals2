vowels = ["a", "e", "i", "o", "u"]

string = list(input())

cons = [x for x in string if x.lower() not in vowels]
print("".join(cons))