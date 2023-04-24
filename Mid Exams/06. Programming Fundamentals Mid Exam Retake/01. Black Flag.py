days = int(input())
daily_plunder = int(input())
expected = float(input())
gained = 0

for day in range(1, days + 1):
    gained += daily_plunder
    if day % 3 == 0:
        gained += daily_plunder * 0.5
    if day % 5 == 0:
        gained *= 0.7

percent = gained / expected
if gained >= expected:
    print(f'Ahoy! {gained:.2f} plunder gained.')
else:
    print(f"Collected only {percent:.2%} of the plunder.")
