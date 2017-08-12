def main():

    str = "hello. my name is Joe. what is your name?"

    def capitalizer(string):

        collector = 0

        index = 0

        determiner = False

        new_string = ""

        for ch in string:
            if index == 0:
                new_string += ch.upper()
            if collector == 2:
                new_string += string[index].upper()
                collector = 0
                determiner = False
            if ch == ".":
                collector += 1
            if collector == 1 and ch == " ":
                collector += 1
            if determiner:
                new_string += ch
            determiner = True
            index += 1

        return new_string

    sentence = capitalizer(str)
    print(sentence)

main()

