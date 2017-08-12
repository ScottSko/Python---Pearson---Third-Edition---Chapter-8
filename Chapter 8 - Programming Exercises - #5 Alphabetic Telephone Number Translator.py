def main():

    str = input("Please enter your telephone number in the format XXX-XXX-XXXX: ")

    converted_string = ""

    sliced = str[0:4]

    converted_string += sliced

    hyphen = 0


    for ch in str[4:]:
        ch = ch.upper()
        if ch == "A" or ch == "B" or ch == "C":
            converted_string += "2"
        if ch == "D" or ch == "E" or ch == "F":
            converted_string += "3"
        if ch == "G" or ch == "H" or ch == "I":
            converted_string += "4"
        if ch == "J" or ch == "K" or ch == "L":
            converted_string += "5"
        if ch == "M" or ch == "N" or ch == "O":
            converted_string += "6"
        if ch == "P" or ch == "Q" or ch == "R" or ch == "S":
            converted_string += "7"
        if ch == "T" or ch == "U" or ch == "V":
            converted_string += "8"
        if ch == "W" or ch == "X" or ch == "Y" or ch == "Z":
            converted_string += "9"
        if hyphen == 2:
            converted_string += "-"
        hyphen += 1

    print("The number is: ", converted_string)

main()