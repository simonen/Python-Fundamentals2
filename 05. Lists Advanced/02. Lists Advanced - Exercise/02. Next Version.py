version = input().split(".")
next_version = int("".join(version)) + 1
final_version = list(str(next_version))
print(".".join(final_version))