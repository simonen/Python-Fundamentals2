electrons = int(input())

capacitor = []
shell = 0
while electrons > 0:
    shell += 1
    per_shell = 2 * shell ** 2
    if electrons >= per_shell:
        capacitor.append(per_shell)
    else:
        capacitor.append(electrons)
    electrons -= per_shell

print(capacitor)
