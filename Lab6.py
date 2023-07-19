## Lab 6 - Miguel Reyes Hello hi

def encode(string):
    new = ''

    for num in string:

        if (int(num) + 3) <= 9:  ## checks if the current num in encode string when added 3 is less than or equal to 9

            new = new + str((int(num) + 3))

        elif (int(num) + 3) == 12:
            new = new + str(2)
        elif (int(num) + 3) == 11:
            new = new + str(1)
        elif (int(num) + 3) == 10:
            new = new + str(0)
    return new

def main():
    while True:

        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n") ## Displays option menu

        option = int(input("Please enter an option: ")) ## prompts user for option input

        if option == 1:

            encode_val = input("Please enter your password to encode: ")  ## prompts user for encode input

            print("Your password has been encoded and stored!\n")

        elif option == 2:

            print(f"The encoded password is {encode(encode_val)}, and the original password is {encode_val}.\n")

        elif option == 3:
            break

