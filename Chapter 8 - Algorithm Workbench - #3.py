def main():

    my_string = "Hello World 123"
    counter = 0

    for ch in my_string:
        if ch.isdigit():
            counter += 1

    print("There are", counter, "digits in your string.")

main()