def every_second_element ():
    first_list = list(map(int , input('Enter a list: ').split()))
    print("Your list:", first_list)
    second_list = first_list[1::2]
    print("Second list(every second element of the first):", second_list)

every_second_element()