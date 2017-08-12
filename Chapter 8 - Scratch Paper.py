def main():

    index = -1

    name = 'Scott'

    reverse_name_string = ''

    first_name = input("Please enter you first name: ")
    middle_name = input("Please enter your middle name: ")
    last_name = input("Please enter your last name: ")

    full_name = (first_name + " " + middle_name + ' ' + last_name)

    print(full_name)

    for ch in full_name:
        reverse_name = full_name[index]
        index -= 1
        reverse_name_string += reverse_name
        print(reverse_name, end='')

    print("\n" + reverse_name_string)

    index_2 = -1

    for str in reverse_name_string:
        corrected_name = reverse_name_string[index_2]
        index_2 -= 1
        print(corrected_name, end='')

main()