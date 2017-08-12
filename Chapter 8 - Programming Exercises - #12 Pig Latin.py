def main():

    str = input("What would you like converted to pig latin? ")

    str = str + " "

    pig_string = ""

    index = 0

    pig_suffix = "ay"

    string_suffix = ""

    for ch in str:
        if index != 0 and ch != " ":
            pig_string += ch
        if index == 0:
            string_suffix = ch
        index += 1
        if ch == " ":
            pig_string += string_suffix
            pig_string += pig_suffix + " "
            index = 0

    print("The pig latin version of your string is", pig_string)

main()
