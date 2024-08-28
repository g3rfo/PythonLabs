string = str(input('Enter somesing: '))
length = len(string)

underscoreNum = string.count('_')

if underscoreNum == 0:
    print("There is no underscore")
else:
    print("There is {} underscore".format(underscoreNum))