def main():

    str = input("What is the string you would like converted to morse code? ")

    if str == ",":
        str = "--..--"

    print("Here is your converted string: ", str)

main()