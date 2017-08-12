def main():

    holder = 0
    backwards_index = -1
    final_value = 0

    my_list = [5, 3, 9, 2, 1, 7]
    sorted_list = [0] * len(my_list)

    #while indicator == "y":

    for num1 in range(len(my_list)):
        for num in my_list:
            if num > holder:
                holder = num
                sorted_list[backwards_index] = holder
            #if num == my_list[backwards_index]:
                #holder = 0
                #backwards_index -= 1
                #sorted_list[backwards_index] = num
        my_list.remove(holder)
        backwards_index -= 1
        holder = 0


    print(sorted_list)

    print(my_list)

main()