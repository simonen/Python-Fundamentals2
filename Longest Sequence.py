def longest_seq(string_f):
    longest = 0
    streak = ''
    prev = ''
    long_streak = ''
    for i in string_f:
        if i != prev:
            streak = ''
        streak += i
        prev = i
        if len(streak) > longest:
            longest = len(streak)
            long_streak = streak

    return long_streak


ticket = 'th@@@@@#4@@@eemo@@@@@@@#@@@ey'
winning_symbols = ["@", "#", "$", "^"]
print(ticket)

longezt_left = longest_seq(ticket[:10])
longezt_right = longest_seq(ticket[10:])
print(longezt_left)
print(longezt_right)

match = min(len(longezt_left), len(longezt_right))
print(f'min: {match}')

print(min(longezt_right, longezt_left))