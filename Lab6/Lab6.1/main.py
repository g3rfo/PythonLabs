def reverse_and_length_calculation_function ():
    our_list = list(map(int , input('Enter a list: ').split()))
    print("Your list:", our_list)
    our_list.reverse()
    print("Reversed list:", our_list)
    print("List length:", len(our_list))

reverse_and_length_calculation_function()