def main():

    my_string = input("Please enter your website name: ")

    def dotcom(string):
        if string.endswith(".com"):
            return True
        else:
            return False

    valid = dotcom(my_string)

    if valid:
        print("Success!")
    else:
        print("Unfortunately, that is not a valid website.")

main()