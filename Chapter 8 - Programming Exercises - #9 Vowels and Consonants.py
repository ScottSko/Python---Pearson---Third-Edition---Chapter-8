def main():

    str = input("Please enter your string: ")

    def vowels(string):

        vowel_counter = 0

        for ch in string:
            ch_u = ch.upper()
            if ch_u == "A" or ch_u == "E" or ch_u == "I" or ch_u == "O" or ch_u == "U":
                vowel_counter += 1

        return vowel_counter

    def consonants(string):

        consonant_counter = 0

        for co in string:
            co_u = co.upper()
            if co_u != "A" and co_u != "E" and co_u != "I" and co_u != "O" and co_u != "U":
                consonant_counter += 1

        return consonant_counter

    v = vowels(str)
    c = consonants(str)

    print("The total number of vowels is", v, "and the total number of consonants is", c)

main()
