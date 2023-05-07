def longest_seq(string_f):
    streak = ''
    prev = ''
    long_streak = ''
    for char in string_f:
        if char != prev:
            streak = ''
        streak += char
        prev = char
        if len(streak) > len(long_streak):
            long_streak = streak

    return long_streak


tickets = input().replace(" ", "").split(",")
winning_symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    left_side = longest_seq(ticket[:10])
    right_side = longest_seq(ticket[10:])
    min_match = min(len(left_side), len(right_side))
    if min_match in range(6, 10) and (left_side[0] in winning_symbols) and (left_side[0] == right_side[0]):
        print(f'ticket "{ticket}" - {min_match}{left_side[0]}')
    elif min_match == 10 and left_side[0] in winning_symbols:
        print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
    else:
        print(f'ticket "{ticket}" - no match')
