def main():

    my_string = "Hello World"
    counter = 0

    for ch in my_string:
        if ch.islower():
            counter += 1

    print("There are", counter, "lowercase characters in your string.")

main()