def main():

    my_string = "Hello    World"
    counter = 0
    for ch in my_string:
        if ch == " ":
            counter += 1

    print("There are", counter, "spaces in your string.")

main()