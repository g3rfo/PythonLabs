arraySize = int(input("Enter the size of the array: "))
print(f"Enter {arraySize} array elements:")
array = [int(input()) for _ in range(arraySize)]
arithmeticMean = 0
positiveNumber = 0
for i in range(arraySize):
    if array[i] > 0:
        positiveNumber += 1
        arithmeticMean += array[i]
print("Arithmetic mean of positive numbers: ", arithmeticMean / positiveNumber)
