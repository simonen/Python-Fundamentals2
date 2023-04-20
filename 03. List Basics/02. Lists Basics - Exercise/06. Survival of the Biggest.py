integers = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    minimal = min(integers)
    integers.remove(minimal)

print(", ".join(list(map(str, integers))))