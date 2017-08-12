def main():

    choice = "y"

    if choice == "y":
        choice = input("y or n?")
        choice = choice.lower()

        if choice == "y":
            print("ok!")
        else:
            print("aww")

main()