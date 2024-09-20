def everySecondElementFunction ():
    firstList = input('Enter a list: ').split()
    print("Your list:", firstList)
    secondList = firstList[1::2]
    print("Second list(every second element of the first):", secondList)

everySecondElementFunction()