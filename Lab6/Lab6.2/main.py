def every_second_element ():
    first_list = list(map(int , input('Enter a list: ').split()))
    print("Your list:", first_list)
    if len(first_list) > 1:
        second_list = first_list[1::2]
        print("Second list(every second element of the first):", second_list)
    else:
        print("Your list too small(< 2)")

every_second_element()