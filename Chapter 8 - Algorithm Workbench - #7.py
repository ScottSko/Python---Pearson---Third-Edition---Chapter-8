def main():

    test = input("What is your string?")

    def backwards(string):
        backwards_index = -1

        new_string = ""

        for ch in string:
            new_string += string[backwards_index]
            backwards_index -= 1

        return new_string

    full_string = backwards(test)

    print(full_string)

main()