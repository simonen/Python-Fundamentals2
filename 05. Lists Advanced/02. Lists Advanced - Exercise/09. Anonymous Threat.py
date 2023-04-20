def merge(s_ind, e_ind, list_f):
    if e_ind not in range(0, len(list_f)):
        e_ind = len(list_f) - 1
    if s_ind not in range(0, len(list_f)):
        s_ind = 0
    list_f[s_ind] = "".join(list_f[s_ind:e_ind + 1])
    list_f = list_f[:s_ind + 1] + list_f[e_ind + 1::]
    return list_f


def divide(string_f, partitions_f):
    if partitions_f > len(string_f):
        partitions_f = len(string_f)
    chunk_size = len(string_f) // partitions_f
    E = []
    for _ in range(1, partitions_f):
        chunk = string_f[:chunk_size]
        E.append(chunk)
        string_f = string_f[chunk_size::]
    E.append(string_f)
    # print(E)
    return E


A = input().split()
command = input()

while command != "3:1":
    command = command.split()
    action = command[0]
    index1 = int(command[1])
    index2 = int(command[2])
    if action == "merge":
        A = merge(index1, index2, A)
    elif action == "divide":
        if index2 in range(1, 101):
            A = A[:index1] + divide(A[index1], index2) + A[index1 + 1:]
    print(A)
    command = input()

print(" ".join(A))
