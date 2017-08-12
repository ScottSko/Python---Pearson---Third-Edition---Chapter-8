def main():

    holder = 0
    backwards_index = -1

    my_list = [1, 1, 5, 3, 9, 2, 1, 7, 9]
    sorted_list = [0] * len(my_list)

    print("The unsorted list is: ", my_list)

    for num1 in range(len(my_list)):
        for num in my_list:
            if num > holder:
                holder = num
                sorted_list[backwards_index] = holder

        my_list.remove(holder)
        backwards_index -= 1
        holder = 0


    print("Your list has been sorted: ", sorted_list)

    #print(my_list)

main()