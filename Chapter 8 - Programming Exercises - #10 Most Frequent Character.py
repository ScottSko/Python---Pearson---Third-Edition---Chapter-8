def main():

    string = "antidisestablishmentarianism"

    string.lower()

    counter = 0
    total_counter = 0

    most_frequent_character = ""

    for ch in string:
        for str in string:
            if str == ch:

                counter += 1
        if counter > total_counter:
            total_counter = counter
            most_frequent_character = ch
        counter = 0

    print("The most frequent character is", most_frequent_character, "and it appears", total_counter, "times.")

main()