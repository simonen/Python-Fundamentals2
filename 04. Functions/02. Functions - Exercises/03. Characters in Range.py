def chars():
    return [chr(x) for x in range(ord(input()) + 1, ord(input()))]


print(" ".join(chars()))
