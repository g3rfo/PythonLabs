matrixSize = 7
matrix = [[(matrixSize)*(i == j) + (matrixSize - j + i)*(i < j) + (matrixSize + j - i)*(i > j) for i in range(matrixSize)] for j in range(matrixSize)]
for row in matrix:
    print(*row)
