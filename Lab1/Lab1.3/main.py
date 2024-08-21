N = int(input("Enter N(1 - 9):"))
while N < 1 or N > 9:
    N = int(input("Invalid value. Enter N again(1 - 9):"))

for i in range(N):
    print(" ")
    for j in range(N):
        if j >= i:
            print(j + 1, end= " ")
        else:
            print(end = "  ")