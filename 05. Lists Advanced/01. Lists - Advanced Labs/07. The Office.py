employees = list(map(int, input().split()))
factor = int(input())

employee_count = len(employees)
new_score = list(map(lambda x: x * factor, employees))
average = sum(new_score) / employee_count
happy_count = len(list(filter(lambda x: x >= average, new_score)))

if happy_count >= employee_count / 2:
    print(f"Score: {happy_count}/{employee_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{employee_count}. Employees are not happy!")
