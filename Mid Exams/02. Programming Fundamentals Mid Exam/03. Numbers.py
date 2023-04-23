seq = list(map(int, input().split()))

average = sum(seq) / len(seq)
sorted_seq = list(filter(lambda x: x > average, sorted(seq, reverse=True)[:5]))

if len(sorted_seq) == 0:
    print("No")
else:
    print(" ".join(list(map(str, sorted_seq))))
