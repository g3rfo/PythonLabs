string = str(input('Enter somesing: '))

length = len(string)

if length < 4:
    print('The sring is too short')
else:
    print("Clipped string:", string[:length-3])