def main():

    str = "StopAndSmellTheRoses"

    index = 0

    converted_string = ""

    for ch in str:
        if ch.isupper() and index != 0:
            converted_string += " "
        converted_string += ch
        index += 1

    cap_string = converted_string.capitalize()

    print(cap_string)


main()