def main():

    index = 0

    #first_name = input("Please enter your first name: ")
    #middle_name = input("Please enter your middle name: ")
    #last_name = input("Please enter your last name: ")

    #first_initial = first_name[0].upper() + "."
    #middle_initial = middle_name[0].upper() + "."
    #last_initial = last_name[0].upper() + "."

    #print("Here are your initials: ", first_initial, middle_initial, last_initial)

    full_name = input("Please enter your full name (with spaces): ")
    f_i = ""
    m_l_i = ""

    for ch in full_name:
        if index == 0:
            f_i = ch.upper() + "." + " "
        if ch == " ":
            index += 1
            m_l_i += full_name[index].upper() + "." + " "
            index += -1

        index += 1

    full = f_i + m_l_i

    print("Your initials are: ", full)

main()