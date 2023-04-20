def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact *= i

    return fact


num1 = int(input())
num2 = int(input())

res = factorial(num1) / factorial(num2)
print(f"{res:.2f}")
