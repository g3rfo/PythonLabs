import math

def function1 (a,b):
    if a >= 15:
        return math.sin(2 * a) + math.cos(2 * b)
    elif a < 0:
        return print("The expression under the root is less than 0")
    else:
        return math.sqrt(a + b ** 2)

def function2 (n):
    result = 0
    for i in range(1, n + 1):
        result += (i + 1)/i
    return result

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Result of function1: ", function1(a,b))

n = int(input("Enter n: "))

print("Result of function2: ", function2(n))