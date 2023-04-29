counting = {}

for i in input().replace(" ", ""):
    if i not in counting:
        counting[i] = 0
    counting[i] += 1

for k, v in counting.items():
    print(f"{k} -> {v}")
