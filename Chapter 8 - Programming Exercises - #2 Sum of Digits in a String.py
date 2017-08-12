def main():

    my_string = input("What is the string of digits you would like to sum? ")

    total = 0

    for ch in my_string:
        ch = int(ch)
        total += ch


    print("Your total is", total)

main()