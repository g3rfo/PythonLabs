a = int(input("Enter a(1 - 100):"))
while a < 1 or a > 100:
    a = int(input("Invalid value. Enter a again(1 - 100):"))

b = int(input("Enter b(1 - 100):"))
while b < 1 or b > 100:
    b = int(input("Invalid value. Enter b again(1 - 100):"))

if a > b:
    x = float(a) / b + 1
elif a == b:
    x = -2
else:
    x = float(a - b) / a

print("X =", x)